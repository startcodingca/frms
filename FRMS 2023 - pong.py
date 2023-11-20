import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FRMS Fall 2023 - Pong")

gameRunning = True
while gameRunning == True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameRunning = False

                                    #where? colour? (xcoor, ycoor, width, height)
    pygame.draw.rect( screen, (166, 58, 205), (0,0,50,100) )

pygame.quit()
