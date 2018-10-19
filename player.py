import collections

class Player :
  def __init__(self, baseHealth, baseMana, baseStrength, baseIntelligence, baseDextery, baseLuck) :
    self.dead = False
    self.lvl = 1

    # Base Stats
    self.baseHealth = baseHealth
    self.baseMana = baseMana
    self.baseStrength = baseStrength
    self.baseIntelligence = baseIntelligence
    self.baseDextery = baseDextery
    self.baseLuck = baseLuck

    # Current Stats
    self.maxHealth = baseHealth
    self.health = baseHealth
    self.maxMana = baseMana
    self.mana = baseMana
    self.strength = baseStrength
    self.intelligence = baseIntelligence
    self.dextery = baseDextery
    self.luck = baseLuck 

    self.healthReg = 0
    self.manaReg = 0

    self.armor = 0
    self.magicResist = 0

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