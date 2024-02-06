import pygame

pygame.init( )
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

bird_y = 300
yspeed = 0

gamerunning = True
while gamerunning == True:
  
  for event in pygame.event.get():
    if pygame.key.get_pressed()[pygame.K_SPACE]:
      yspeed = -25

  bird_y = bird_y + yspeed
  yspeed += 1.65
  
  screen.fill((204, 230, 255))
  pygame.draw.rect(screen, (0,0,0), (300, bird_y, 40, 40))
  pygame.display.update()
  clock.tick(25)
  
