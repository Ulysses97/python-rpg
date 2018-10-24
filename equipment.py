
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

  def equip(self, player) :
    # El Jugador se equipa el item.
    player.equipment[self.type] = self

  def unequip(self, player) :
    # Si el item cabe en el inventario, se guardará. Sino, el item se perderá.
    if self.size <= player.inventory['availableSlots'] :
      player.inventory['inventory'].append(self)
      player.inventory['availableSlots'] -= self.size

    player.equipment[self.type] = None
    return self