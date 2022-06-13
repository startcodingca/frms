import pygame

W = 800
H = 600

LGREY = (240,240,240)
BLACK = (0,0,0)
BLUE = (34,129,209)
RED = (255,0,0)

#starting up pygame
print(pygame.init())

#set up game window
screen = pygame.display.set_mode((W, H))

#BALL VARIABLES
ballx = W/2 #400
bally = H/2

#game loop
gameLoop = True
while gameLoop == True:
  
  ballx = ballx + 0.01
  
  screen.fill(LGREY)
  pygame.draw.rect(screen, RED, (ballx,bally,25,25))
  pygame.display.update() #render