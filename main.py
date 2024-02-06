import pygame

pygame.init( )

screen = pygame.display.set_mode((800,600))

gamerunning = True
while gamerunning == True:
  
  screen.fill((204, 230, 255))
  pygame.draw.rect(screen, (0,0,0), (0, 0, 400, 400))
  pygame.display.update()
  