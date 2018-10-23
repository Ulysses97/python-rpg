
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
    # Las estadísticas del item se suman a las del Jugador.
    for p_key, p_value in player.currentStats.items() :
      for key, value in self.stats.items() :
        if key == p_key and value != 0 :
          player.currentStats[key] = p_value + value