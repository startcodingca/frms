import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

playerX = 375

gameLoop = True
while gameLoop == True:
  
  for event in pygame.event.get():
    if pygame.key.get_pressed()[pygame.K_d]:
      print("Move right")
      playerX = playerX + 10
  
  screen.fill((186, 248, 255))
  pygame.draw.rect(screen, (0,0,0), (playerX,250,50,100))
  pygame.display.update() #rendering
