import pygame

W = 800
H = 600

LGREY = (240,240,240)
BLACK = (0,0,0)
BLUE = (34,129,209)
RED = (255,0,0)

BALLSIZE = 25

#starting up pygame
print(pygame.init())

#set up game window
screen = pygame.display.set_mode((W, H))

#BALL VARIABLES
ballx = W/2 #400
bally = 0

ballspeedx = 0.2
ballspeedy = 0.2

p1x = 20
p1y = H/2

PADDLEW = 25
PADDLEH = 100

#game loop
gameLoop = True
while gameLoop == True:
  
  #BALL X BOUNCE
  if ballx > W: #leaves right of screen
    ballspeedx = -0.2
  elif ballx < 0:
    ballspeedx = 0.2
  
  ballx = ballx + ballspeedx
  
  #BALL Y BOUNCE
  if bally > H:
    ballspeedy = -0.2
  elif ballx < 0:
    ballspeedy = 0.2
  
  bally = bally + ballspeedy
  
  screen.fill(LGREY)
  pygame.draw.rect(screen, RED, (ballx,bally,BALLSIZE,BALLSIZE))
  pygame.draw.rect(screen, BLUE, (p1x, p1y, PADDLEW, PADDLEH))
  pygame.display.update() #render