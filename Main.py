import random
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
    def __init__(self,monster):
      self.health = 15
      self.name = input('what is your name?')
      self.stamina = 100
      hero.name = name
    def (help):
        print('Here are your list of commands:')
        print('1. Help. 2.Explore. 3.run. 4.Fight')
    def (explore):
        print(hero.name, 'Has gone Exploring! you will soon be faced with', monster.name)
        print('Stamina: ', stamina.amount, ' Health: ', health.amount)
    def (run):
        print('you Have ran from ', monster.name, 'and as a result, your stamina has decreased by 10')
        stamina.amount = stamina.amount - 10
        print('stamina: ', stamina.amount)
    def (fight):
        print('You have fought', monster.name)
        self.health = random.randint(0,5)
        print('Your Health Currently: ', self.health)
  
  
class Monster(LivingCreature):
    def __init__ (self,monster):
        self.health = 15
        self.name = name
        Goblin=Monster('Goblin',20)
        Zombie=Monster('Zombie',15)
        Monster=[]
        Goblin.append
        Zombie.append
        Monsters= random.choice(Monster)
        
Commands = {
 'help', Player.help,
 'explore', Player.explore,
 'run', Player.run,
 'fight', Player.fight,
 }
 

    