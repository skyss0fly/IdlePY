import random

class LivingCreature():
  def __init__(self, name):
      self.name = name
      self.health = 1
      
class Player(LivingCreature):
    def __init__(self, name, monster):
      super().__init__(name)
      self.health = 15
      self.stamina = 100
      self.monster = monster
      self.cash = 0
    def cash(self):
      print(self.cash)
    
    def inventory(self):
      print('inventory')
      self.items = 0
      
    def shop(self):
      print('Shop Items:')
    def help(self):
        print('Here are your list of commands:')
        print('1. Help. 2.Explore. 3.run. 4.Fight. 5. Cash')
        
    def explore(self):
        print(self.name, 'Has gone Exploring! you will soon be faced with', self.monster.name)
        print('Stamina: ', self.stamina, ' Health: ', self.health)
        print('you have earned 1 Cash for Exploring ')
        cash.value + 1
        print('Current Cash: ', self.cash)
        
      
        
    def run(self):
        print('you Have ran from ', self.monster.name, 'and as a result, your stamina has decreased by 10')
        self.stamina -= 10
        print('stamina: ', self.stamina)
        
    def fight(self):
        print('You have fought', self.monster.name, ' and gained 5 cash')
        cash.value = cash.value + 5
        self.health -= random.randint(0,5)
        print('Your Health Currently: ', self.health)
  
  
class Monster(LivingCreature):
    def __init__ (self, name, health):
        super().__init__(name)
        self.health = health

goblin = Monster('Goblin', 20)
zombie = Monster('Zombie', 15)
monsters = [goblin, zombie]
chosen_monster = random.choice(monsters)

commands = {
 'help': Player.help,
 'explore': Player.explore,
 'run': Player.run,
 'fight': Player.fight,
 'inventory' : Player.inventory,
 'shop' : Player.shop,
 'cash' : Player.cash,
 }

player_name = input('what is your name?')
player = Player(player_name, chosen_monster)

while True:
    user_input = input('What would you like to do? ')
    command = commands.get(user_input)
    if command:
        command(player)
    else:
        print('Invalid command. Type "help" to see available commands.')
