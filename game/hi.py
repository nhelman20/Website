import sys, pygame
pygame.init()
 
size = width, height = 956, 637
black = 0, 0, 0

screen = pygame.display.set_mode(size)

logo = pygame.image.load("logo.gif")
logorect = logo.get_rect()
while 1:
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(logo, logorect)
    pygame.display.flip()
    
    
    
    
    
    
    
    
    
