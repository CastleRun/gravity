class Position(object):
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

class Planet(object):
  def __init__(self, mass, x, y, z, vx, vy, vz):
    self.mass = mass
    self.pos = new Position(x,y,z)
    self.vector = new Position(vx, vy, xz)
  
  def push(x, y, z):
    self.vector.x += x
    self.vector.y += y
    self.vector.z += z
  
  def update(self):
    self.pos.x += self.vector.x
    self.pos.y += self.vector.y
    self.pos.z += self.vector.z
