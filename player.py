import collections

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
      'luck' : baseLuck
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
      'magicResist' : 0,
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

  def equipItemFromInventory(self, item) :
    item.equip(self) # Las estadísticas del item se suman a las del Jugador.
    self.inventory['inventory'].remove(item) # El item es removido del inventario.
    self.inventory['availableSlots'] += item.size # Se libera espacio en el inventario.