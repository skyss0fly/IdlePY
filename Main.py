class LivingCreature():
  def __init__(self):
    self.name = 'Name'
  def __init__(health):
   self.health = 1
  def __init__(tire):
    self.health = self.health - 1
  def __init__(hurt):
    self.health = self.health - 1

class Player(LivingCreature):
    def __init__(self, monster):
    self.health = 15
    self.name = input('what is your name?')
    self.stamina = 100


class Monster(LivingThing):
    def __init__ (self,monster):
        self.health = 15
        self.name = name
        self.Damage = Damage

Commands = {
 'help', Player.help,
 'explore', Player.explore,
 'run', Player.explore,
 'fight', Player.fight,
    }

   
