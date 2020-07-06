class Animal():
  def __init__(self, age : int, height : int, name : str, colour : str):
    self.age = age
    self.height = height
    self.name = name
    self.colour = colour

  def getDescription(self):
    return f'Age: {self.age}\nName: {self.name}\nColour: {self.colour}'
  
  def ageTimeHeight(self):
    return self.age * self.height

class Bus():
  def __init__(self, properties : str, height : int, length : int, busAgency : str):
    self.properties = properties
    self.height = height
    self.length = length
    self.busAgency = busAgency

  def getMaxPeople(self):
    return self.height * self.length
  
  def setbusAgency(self, busAgency : str):
    self.busAgency = busAgency

cat = Animal(5, 30, 'kitty', 'grey')
cat.ageTimeHeight
cat.getDescription