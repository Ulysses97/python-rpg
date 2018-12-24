
# Gema -> tipo : p/a/c (pasiva/activa/cualquiera) + o/d/c (ofensiva/defensiva/cualquiera)

class Gem :
  def __init__(self, _type, name, size, stats, multipliers, lvl_needed) :
    self.type = _type
    self.name = name
    self.size = size
    self.lvl_needed = lvl_needed

    self.stats = stats
    self.multipliers = multipliers

  def equip(self, equipment) :
    for socket in equipment.sockets :
      if socket.type[0] in ['c', self.type[0]] and socket.type[1] in ['c', self.type[1]] :
        socket.equipGem(self)
        print(self.name + " equipada.")
        return True
    print("No posees ranuras compatibles para equipar esta gema.")
    return False

  def unequip(self, equipment) :
    for socket in equipment.sockets :
      if socket.gem == self :
        socket.gem = None
        print("Gema desequipada.")
