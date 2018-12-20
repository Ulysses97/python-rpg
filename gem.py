
class Gem :
  def __init__(self, _type, name) :
    self.type = _type
    self.name = name

  def equip(self, equipment) :
    for socket in equipment.sockets :
      if socket.type[0] in ['c', self.type[0]] and socket.type[1] in ['c', self.type[1]] :
        socket.equipGem(self)
        return
    print("No posees ranuras para equipar esta gema.")
