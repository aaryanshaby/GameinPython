import pygame

#initialise pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600))


#Title and icon
pygame.display.set_caption("The Battle of the Morannon")
icon =pygame.image.load('onering.png')
pygame.display.set_icon(icon)
#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    #background color
    screen.fill((255, 0, 50))
    pygame.display.update()