
class Socket :
  def __init__(self, _type) :
    self.type = _type
    self.gem = None

  def equipGem(self, gem) :
    self.gem = gem

  def unequipGem(self) :
    self.gem = None

class Equipment :
  def __init__(self, _type, size, name, health, mana, healthReg, manaReg, strength, intelligence, dextery, luck, armor, magicResist) :
    self.type = _type
    self.size = size
    self.name = name

    self.stats = {
      'maxHealth' : health,
      'maxMana' : mana,
      'healthReg' : healthReg,
      'manaReg' : manaReg,
      'strength' : strength,
      'intelligence' : intelligence,
      'dextery' : dextery,
      'luck' : luck,
      'armor' : armor,
      'magicResist' : magicResist 
    }

    if self.type == 'head' :
      self.sockets = [Socket('pc')]
    elif self.type == 'chest' :
      self.sockets = [Socket('cc'), Socket('cc')]
    elif self.type == 'legs' :
      self.sockets = [Socket('pc')]
    elif self.type == 'leftArm' :
      self.sockets = [Socket('ad')]
    elif self.type == 'rightArm' :
      self.sockets = [Socket('ao')]
    elif self.type == 'amulet' :
      self.sockets = [Socket('cc')]
    elif self.type == 'leftRing' :
      self.sockets = [Socket('pc')]
    elif self.type == 'rightRing' :
      self.sockets = [Socket('pc')]

  def equip(self, player) :
    player.equipment[self.type] = self

  def unequip(self, player) :
    player.equipment[self.type] = None
    return self