
class Socket :
  def __init__(self, _type) :
    self.type = _type
    self.gem = None

  # Asumimos que el equipar desde el inventario, remover y añadir al inventario,
  # será manejado por otros métodos.
  def equipGem(self, gem) :
    self.gem = gem

  def unequipGem(self) :
    self.gem = None

class Equipment :
  def __init__(self, _type, size, name, stats, multipliers, lvl_needed) :
    self.type = _type
    self.size = size
    self.name = name
    self.lvl_needed = lvl_needed

    # Estadísticas :
    #  -maxHealth
    #  -maxMana
    #  -healthReg
    #  -manaReg
    #  -strength
    #  -intelligence
    #  -dextery
    #  -luck
    #  -armor
    #  -magicResist

    self.stats = stats

    self.multipliers = multipliers

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