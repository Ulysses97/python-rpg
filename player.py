import collections

###
import importlib
equipment = importlib.import_module("equipment")
gem = importlib.import_module("gem")
###

# Constantes :
STARTING_LVL = 1
FIRST_LVL_UP_EXP = 500
INCREASE_RATE = 0.15
POINTER_PER_LVLUP = 5
STARTING_SLOTS = 10

class Player :
  def __init__(self, name, baseStats) :
    self.dead = False
    self.lvl = STARTING_LVL
    self.name = name

    self.currentExp = 0
    self.exp_to_lvlUp = FIRST_LVL_UP_EXP

    # Estadísticas base :
    #  -maxHealth
    #  -maxMana
    #  -health
    #  -mana
    #  -strength
    #  -intelligence
    #  -dextery
    #  -luck

    #  -healthReg
    #  -manaReg

    #  -armor
    #  -magicResist

    self.baseStats = baseStats

    # Estadísticas actuales
    self.currentStats = baseStats

    # Multiplicadores : tupla ('stat', %) 
    self.multipliers = []

    # Equipamiento
    self.equipment = [
      ('head', None),
      ('chest', None),
      ('legs', None),
      ('leftArm', None),
      ('rightArm', None),
      ('amulet', None),
      ('leftRing', None),
      ('rightRing', None)
    ]
    self.equipment = collections.OrderedDict(self.equipment)

    # Inventario
    self.inventory = {
      'inventory' : list(),
      'maxSlots' : STARTING_SLOTS,
      'availableSlots' : STARTING_SLOTS
    }

  def resetStats(self) :
    # Reinicia las estadísticas del jugador a las estadísticas base.
    self.currentStats = self.baseStats.copy()

  def healUp(self) :
    # Setea la vida y maná al máximo.
    self.currentStats['health'] = self.currentStats['maxHealth']
    self.currentStats['mana'] = self.currentStats['maxMana']

  def roundStats(self) :
    for key, value in self.currentStats.items() :
      self.currentStats[key] = round(value)

  def calcStats(self) :
    # Calcula las estadísticas del jugador, sumadas las estadísticas de su equipamiento.
    self.resetStats()
    for _type, item in self.equipment.items() :
      if item != None :
        for key, value in item.stats.items() : # Stats del item.
          self.currentStats[key] += value

        for socket in item.sockets : # Stats de sus gemas.
          if socket.gem != None :
            for key, value in socket.gem.stats.items() :
              self.currentStats[key] += value

    # Luego se aplican los multiplicadores.
    for stat, percentage in self.multipliers :
      self.currentStats[stat] += (percentage * self.currentStats[stat])

    self.roundStats()
    self.healUp()

  def addMultipliers(self, item) :
    self.multipliers.extend(item.multipliers)

  def deleteMultipliers(self, item) :
    for mult in item.multipliers :
      self.multipliers.remove(mult)

  def removeItem(self, item) :
    self.inventory['inventory'].remove(item) # El item es removido del inventario.
    self.inventory['availableSlots'] += item.size # Se libera espacio en el inventario.

  def appendItem(self, item) :
    # Asumiendo que el item cabe en el inventario!
    self.inventory['inventory'].append(item) # Se agrega al inventario.
    self.inventory['availableSlots'] -= item.size # Se actualizan los espacios disponibles en el inventario.

  def equipItemFromInventory(self, item) :
    if self.lvl >= item.lvl_needed :
      if self.equipment[item.type] != None : # Existe un item ya equipado.
        if self.inventory['availableSlots'] + item.size < self.equipment[item.type].size :
          # El item equipado no cabe en el inventario, de proceder este se perderá.
          choice = str(input('El item equipado actualmente no cabe en el inventario, de proceder este se perderá. ¿Continuar? (y/n) : ')).lower()
          while choice not in ['y','n'] :
            choice = str(input('Ingresa una opción válida (y/n) : ')).lower()

          if choice == 'n' :
            return
        else :
          unequippedItem = self.equipment[item.type].unequip(self) # El item es desequipado y guardado en el inventario.
          self.appendItem(unequippedItem)

      item.equip(self)
      self.removeItem(item)
      self.addMultipliers(item)
      self.calcStats()
    else :
      print("No posees el nivel necesario para equiparte este objeto.")

  def equipFromGround(self, item) :
    if self.lvl >= item.lvl_needed :
      if self.equipment[item.type] != None : # Existe un item ya equipado.
        if self.equipment[item.type].size > self.inventory['availableSlots'] :
          # El item equipado no cabe en el inventario, de proceder este se perderá.
          choice = str(input('El item equipado actualmente no cabe en el inventario, de proceder este se perderá. ¿Continuar? (y/n) : ')).lower()
          while choice not in ['y','n'] :
            choice = str(input('Ingresa una opción válida (y/n) : ')).lower()

          if choice == 'n' :
            return
        else :
          unequippedItem = self.equipment[item.type].unequip(self) # El item es desequipado y guardado en el inventario.
          self.appendItem(unequippedItem)
      item.equip(self)
      self.addMultipliers(item)
      self.calcStats()
    else :
      print("No posees el nivel necesario para equiparte este objeto.")

  def unequipItem(self, item) :
    if self.inventory['availableSlots'] < item.size :
      # El item que se desea desequipar no cabe en el inventario.
      choice = str(input('El item equipado actualmente no cabe en el inventario, de proceder este se perderá. ¿Continuar? (y/n) : ')).lower()
      while choice not in ['y','n'] :
        choice = str(input('Ingresa una opción válida (y/n) : ')).lower()

      if choice == 'n' :
        return
      else :
        item.unequip(self)
    else :
      self.appendItem(item)
      item.unequip(self)
    self.deleteMultipliers(item)
    self.calcStats()

  def pickItem(self, item) :
    if item.size <= self.inventory['availableSlots'] :
      self.appendItem(item)
      print(item.name + " recogido.")
    else :
      print("No tienes espacio suficiente para llevar este objeto.")

  def dropItem(self, item) :
    choice = str(input("Si sueltas un objeto, este se perderá. ¿Estás seguro? (y/n) : ")).lower()
    while choice not in ['y','n'] :
      choice = str(input("Ingresa una opción válida (y/n) : ")).lower()

    if choice == 'n' :
      return
    else :
      self.removeItem(item)

  def equipGem(self, equipment, gem) :
    # Desde el inventario. No se puede equipar desde el suelo.
    if self.lvl >= gem.lvl_needed :
      if gem.equip(equipment) : # Si se ha equipado:
        self.removeItem(gem) # Remover del inventario.
        self.addMultipliers(gem)
        self.calcStats()
    else :
      print("No posees el nivel necesario para equiparte esta gema.")

  def unequipGem(self, equipment, gem) :
    if self.inventory['availableSlots'] < gem.size :
      # La gema no cabe en el inventario.
      choice = str(input('La gema equipada actualmente no cabe en el inventario, de proceder esta se perderá. ¿Continuar? (y/n) : ')).lower()
      while choice not in ['y','n'] :
        choice = str(input('Ingresa una opción válida (y/n) : ')).lower()

      if choice == 'n' :
        return
      else :
        gem.unequip(equipment)
    else :
      self.appendItem(gem)
      gem.unequip(equipment)
    self.deleteMultipliers(gem)
    self.calcStats()

#############

jugador = Player("Ulises", {
  'maxHealth' : 1000,
  'maxMana' : 200,
  'health' : 1000,
  'mana' : 200,
  'strength' : 10,
  'intelligence' : 10,
  'dextery' : 10,
  'luck' : 0,
  'healthReg' : 0,
  'manaReg' : 0,
  'armor' : 0,
  'magicResist' : 0,
}) 
casco = equipment.Equipment("head",2,"Casco",{
  'maxHealth' : 200,
  'maxMana' : 100,
  'healthReg' : 1,
  'manaReg' : 1,
  'strength' : 10,
  'intelligence' : 10,
  'dextery' : 10,
  'luck' : 0,
  'armor' : 20,
  'magicResist' : 10 
},[],1)
gema = gem.Gem("pc", "Gema Pasiva Común",1, {
  'maxHealth' : 100,
  'maxMana' : 0,
  'healthReg' : 0,
  'manaReg' : 0,
  'strength' : 0,
  'intelligence' : 0,
  'dextery' : 0,
  'luck' : 0,
  'armor' : 10,
  'magicResist' : 0 
},[('maxHealth',0.02)],2)

peto = equipment.Equipment("chest",2,"Peto",{
  'maxHealth' : 200,
  'maxMana' : 100,
  'healthReg' : 1,
  'manaReg' : 1,
  'strength' : 10,
  'intelligence' : 10,
  'dextery' : 10,
  'luck' : 0,
  'armor' : 20,
  'magicResist' : 10 
},[('maxHealth',0.02)],1)

jugador.pickItem(casco)
jugador.pickItem(gema)
jugador.pickItem(peto)

jugador.equipItemFromInventory(casco)
jugador.equipGem(casco, gema)
jugador.equipItemFromInventory(peto)

#print(jugador.currentStats)

jugador.unequipGem(casco, gema)
jugador.unequipItem(casco)

#print(jugador.currentStats)