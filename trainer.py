class Trainer:
  def __init__(self, name, money, jorgemons):
    self.name = name
    self.money = money
    self.jorgemons = jorgemons

  def list_jorgemons(self):
    print("{}'s jorgemons".format(self.name))
    for c in self.jorgemons:
      print(c.na