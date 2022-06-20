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

ballspeedx = 1
ballspeedy = 1

p1x = 20
p1y = H/2
p1speed = 0

PADDLEW = 25
PADDLEH = 100

#game loop
gameLoop = True
while gameLoop == True:

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        p1speed = -10
      if event.key == pygame.K_s:
        p1speed = 10

    if event.type == pygame.KEYUP:
      p1speed = 0
  
  #p1 movement
  p1y = p1y + p1speed
  
  #BALL X BOUNCE
  if ballx > W: #leaves right of screen
    ballspeedx = -1
  elif ballx < 0:
    ballspeedx = 1
  
  ballx = ballx + ballspeedx
  
  #BALL Y BOUNCE
  if bally > H:
    ballspeedy = -1
  elif ballx < 0:
    ballspeedy = 1
  
  bally = bally + ballspeedy
  
  screen.fill(LGREY)
  pygame.draw.rect(screen, RED, (ballx,bally,BALLSIZE,BALLSIZE))
  pygame.draw.rect(screen, BLUE, (p1x, p1y, PADDLEW, PADDLEH))
  pygame.display.update() #render