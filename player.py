import collections
####################### Testing
import importlib
equipment = importlib.import_module("equipment")
##########################

class Player :
  def __init__(self, baseHealth, baseMana, baseStrength, baseIntelligence, baseDextery, baseLuck) :
    self.dead = False
    self.lvl = 1

    # Base Stats
    self.baseStats = {
      'health' : baseHealth,
      'mana' : baseMana,
      'strength' : baseStrength,
      'intelligence' : baseIntelligence,
      'dextery' : baseDextery,
      'luck' : baseLuck,

      'healthReg' : 0,
      'manaReg' : 0,

      'armor' : 0,
      'magicResist' : 0
    }

    # Current Stats
    self.currentStats = {
      'maxHealth' : baseHealth,
      'health' : baseHealth,
      'maxMana' : baseMana,
      'mana' : baseMana,
      'strength' : baseStrength,
      'intelligence' : baseIntelligence,
      'dextery' : baseDextery,
      'luck' : baseLuck,

      'healthReg' : 0,
      'manaReg' : 0,

      'armor' : 0,
      'magicResist' : 0
    }

    # Equipment
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

    # Inventory
    self.inventory = {
      'inventory' : list(),
      'maxSlots' : 10,
      'availableSlots' : 10
    }

  def resetStats(self) :
    # Reinicia las estadísticas del jugador a las estadísticas base.
    for key, value in self.baseStats.items() :
      if key == 'health' :
        self.currentStats['maxHealth'] = value
      elif key == 'mana' :
        self.currentStats['maxMana'] = value
      self.currentStats[key] = value

  def healUp(self) :
    # Setea la vida y maná al máximo.
    self.currentStats['health'] = self.currentStats['maxHealth']
    self.currentStats['mana'] = self.currentStats['maxMana']

  def calcStats(self) :
    # Calcula las estadísticas del jugador, sumadas las estadísticas de su equipamiento.
    self.resetStats()
    for _type, item in self.equipment.items() :
      if item != None :
        for key, value in item.stats.items() :
          self.currentStats[key] += value

    self.healUp()

  def removeItem(self, item) :
    self.inventory['inventory'].remove(item) # El item es removido del inventario.
    self.inventory['availableSlots'] += item.size # Se libera espacio en el inventario.

  def appendItem(self, item) :
    # Asumiendo que el item cabe en el inventario!
    self.inventory['inventory'].append(item) # Se agrega al inventario.
    self.inventory['availableSlots'] -= item.size # Se actualizan los espacios disponibles en el inventario.

  def equipItemFromInventory(self, item) :
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
    self.calcStats()

  def equipFromGround(self, item) :
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
    self.calcStats()

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

################################ testing
# jugador = Player(1,1,1,1,1,1)
# casco = equipment.Equipment('head',8,'casco',1,1,1,1,1,1,1,1,1,1)
# jugador.inventory['inventory'].append(casco)
# jugador.inventory['availableSlots'] -= casco.size

# jugador.equipItemFromInventory(jugador.inventory['inventory'][0])

# casco2 = equipment.Equipment('head',5,'casco2',1,1,1,1,1,1,1,1,1,1)

# jugador.inventory['inventory'].append(casco2)
# jugador.inventory['availableSlots'] -= casco2.size

# botas = equipment.Equipment('legs',5,'botas',1,1,1,1,1,1,1,1,1,1)

# jugador.inventory['inventory'].append(botas)
# jugador.inventory['availableSlots'] -= botas.size

# casco3 = equipment.Equipment('head',5,'casco3',1,1,1,1,1,1,1,1,1,1)

# jugador.equipFromGround(casco3)

# print(jugador.inventory['inventory'])