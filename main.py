import pygame
import random
# initialise pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((1000, 800))

# Title and icon
pygame.display.set_caption(" The Battle of the Morannon")
icon = pygame.image.load('onering.png')
pygame.display.set_icon(icon)

# player1 = gondorians
player1img = pygame.image.load('player1.png')
player1X = 460
player1Y = 700
enemyfor1X_change = 0
enemyfor1Y_change = 0

# enemy
enemyfor1img = pygame.image.load('orc1.png')
enemyfor1X = random.randint(0,900)
enemyfor1Y = random.randint(0,600)
player1X_change = 0
player1Y_change = 0


def player1(x, y):
    screen.blit(player1img, (x, y))


def enemyfor1(x, y):
    screen.blit(enemyfor1img, (x, y))


# Game loop
running = True
while running:
    # background color
    screen.fill((91, 49, 0))
    for event in pygame.event.get():

        # for Quiting
        if event.type == pygame.QUIT:
            running = False

        # check pressed key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow is preesed")
                player1X_change = -0.1
            if event.key == pygame.K_RIGHT:
                print("right arrow is preesed")
                player1X_change = 0.1
            if event.key == pygame.K_UP:
                print("up arrow is preesed")
                player1Y_change = -0.1
            if event.key == pygame.K_DOWN:
                print("down arrow is preesed")
                player1Y_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                print("l R arrow is released")
                player1X_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("u d is released")
                player1Y_change = 0

    player1X += player1X_change
    player1Y += player1Y_change

    if player1X < 0 or player1X > 939:
        player1X_change = 0
    if player1Y < 0 or player1Y > 730:
        player1Y_change = 0
    player1(player1X, player1Y)
    enemyfor1(enemyfor1X,enemyfor1Y)
    pygame.display.update()
