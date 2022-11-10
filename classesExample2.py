import math

class Circle:

  def __init__(self, radius):
    self.radius = radius
 
  def calculatearea(self):
    return math.pi*self.radius**2

  def calculatecircumference(self):
      return 2*math.pi*self.radius

p1 = Circle(7)

print(type(p1))

print(p1.calculatearea())

print(p1.calculatecircumference())

