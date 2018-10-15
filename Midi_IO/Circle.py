class Circle:
  def __init__(self, radius = None):
    if radius != None:
      self.__radius = radius
    else:
      self.__radius = 10

  def getRadius(self):
    return self.__radius

  def setRadius(self, radius):
    self.__radius = radius
