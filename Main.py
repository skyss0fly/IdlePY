import pygame
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
      self.x = 0
      self.y = 0
      self.z = 0
    
    def cash(self):
      print(self.cash)
    
    def inventory(self):
      print('inventory')
      self.items = 0
      
    def shop(self):
      print('Shop Items:')
      
    def help(self):
        print('Here are your list of commands:')
        print('1. Help. 2.Explore. 3.run. 4.Fight. 5. Cash. 6. Move')
        
    def explore(self):
        print(self.name, 'Has gone Exploring! you will soon be faced with', self.monster.name)
        print('Stamina: ', self.stamina, ' Health: ', self.health)
        print('you have earned 1 Cash for Exploring ')
        cash.value + 1
        print('Current Cash: ', self.cash)
        
    def move(self):
        direction = input('Select a direction: up, down, left, right')
        if(direction == 'up'):
            self.y += 1
        elif(direction == 'down'):
            self.y -= 1
        elif(direction == 'left'):
            self.x -= 1
        elif(direction == 'right'):
            self.x += 1
        else:
            print('Invalid direction')
        print('Position: ', self.x, self.y, self.z)
        
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
 'move' : Player.move
 }

player_name = input('what is your name?')
player = Player(player_name, chosen_monster)

#pygame setup
pygame.init()
#Screen Setup
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width,screen_height))

#Title and Icon
pygame.display.set_caption("3D Game")

#Game Loop
running = True
while running:
    user_input = input('What would you like to do? ')
    command = commands.get(user_input)
    if command:
        command(player)
    else:
        print('Invalid command. Type "help" to see available commands.')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
