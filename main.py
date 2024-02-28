#left off doing game over text. made font and text, need to render at ground collision

import pygame, random, time

pygame.init( )
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

score = 0

scorefont = pygame.font.Font('freesansbold.ttf', 50)
birdScoreFont = scorefont.render("Score: " + str(score), True, (0,0,0), None)
birdScoreRect = birdScoreFont.get_rect()
birdScoreRect.center = (0,0)

gameoverfont = pygame.font.Font('freesansbold.ttf', 200)
gameoverText = gameoverfont.render("GAME OVER.", True, (255,0,0), None)

bird_x = 300
bird_y = 300
yspeed = 0
canJump = True

pipe_x = 800
pipe_y = random.randint(350, 550)


gamerunning = True
while gamerunning == True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gamerunning = False

    if pygame.key.get_pressed()[pygame.K_SPACE] and canJump == True:
      yspeed = -25
      canJump = False

    elif not pygame.key.get_pressed()[pygame.K_SPACE]:
      canJump = True

  bird_y = bird_y + yspeed
  yspeed += 1.65

  if pipe_x < -100:
    score = score + 1
    birdScoreFont = scorefont.render("Score: " + str(score), True, (0,0,0), None)
    pipe_x = 900
    pipe_y = random.randint(350,550)

  pipe_x -= 8 

  #======COLLISIONS======
  #GROUND COLLISION
  if bird_y >= 560:
    time.sleep(2)
    gamerunning = False

  #LOWER PIPE COLLISION
  elif bird_x + 40 > pipe_x and bird_x < pipe_x + 100 and bird_y + 40 > pipe_y:
    gamerunning = False

  #UPPER PIPE COLLISION
  elif bird_x + 40 > pipe_x and bird_x < pipe_x + 100 and bird_y < pipe_y - 250:
    gamerunning = False
  
  #=====RENDERINGS=======
  screen.fill((204, 230, 255))
  pygame.draw.rect(screen, (0,0,0), (bird_x, bird_y, 40, 40))
  pygame.draw.rect(screen, (0,255,0), (pipe_x, pipe_y, 100, 600))
  pygame.draw.rect(screen, (0,255,0), (pipe_x, pipe_y - 600 - 250, 100, 600))
  screen.blit(birdScoreFont, (0,0))
  pygame.display.update()
  clock.tick(25)

pygame.quit()

