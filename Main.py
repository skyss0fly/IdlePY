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
      
    def help(self):
        print('Here are your list of commands:')
        print('1. Help. 2.Explore. 3.run. 4.Fight')
        
    def explore(self):
        print(self.name, 'Has gone Exploring! you will soon be faced with', self.monster.name)
        print('Stamina: ', self.stamina, ' Health: ', self.health)
        
    def run(self):
        print('you Have ran from ', self.monster.name, 'and as a result, your stamina has decreased by 10')
        self.stamina -= 10
        print('stamina: ', self.stamina)
        
    def fight(self):
        print('You have fought', self.monster.name)
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
