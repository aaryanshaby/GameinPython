import pygame
import random
import math

# initialise pygame
# comment by divyansh
pygame.init()

# creating the screen
screen = pygame.display.set_mode((1000, 800))

# Title and icon
pygame.display.set_caption(" The Battle of the Morannon")
icon = pygame.image.load('onering.png')
pygame.display.set_icon(icon)


def randomXgenerate(x, y):
    return random.randint(x, y)


# player1 = gondorians
player1img = pygame.image.load('player1.png')
player1X = 460
player1Y = 720
enemyfor1X_change = 0
enemyfor1Y_change = 0
a = 92
b = 140
c = 10
# enemy
enemyfor1img = pygame.image.load('orc1.png')
enemyfor2img = pygame.image.load('snake.png')
enemyfor3img = pygame.image.load('orc2.png')
enemyfor4img = pygame.image.load('dragon.png')
enemyfor5img = pygame.image.load('spider.png')
enemyfor1X = random.randint(0, 900)
enemyfor1Y = 80
enemyfor2X = random.randint(0, 900)
enemyfor2Y = 340
enemyfor3X = random.randint(0, 900)
enemyfor3Y = 590
# enemyfor4X = random.randint(0,900)
# enemyfor4Y = 0
# enemyfor5X = random.randint(0,900)
# enemyfor5Y = 0
enemyfor11X = random.randint(0, 900)
enemyfor11Y = 150
enemyfor21X = random.randint(0, 900)
enemyfor21Y = 400
enemyfor31X = random.randint(0, 900)
enemyfor31Y = 650
# enemyfor41X = random.randint(0,900)
# enemyfor41Y = 0
# enemyfor51X = random.randint(0,900)
# enemyfor51Y = 0

fixedobstacle1X = randomXgenerate(0, 350)
fixedobstacle1Y = 210

fixedobstacle2X = randomXgenerate(0, 350)
fixedobstacle2Y = 450

fixedobstacle3X = randomXgenerate(390, 900)
fixedobstacle3Y = 210

fixedobstacle4X = randomXgenerate(390, 900)
fixedobstacle4Y = 450

fixedobstacle01X = randomXgenerate(450, 900)
fixedobstacle01Y = 10

fixedobstacle02X = randomXgenerate(0, 300)
fixedobstacle02Y = 730

player1X_change = 0
player1Y_change = 0
enemyspeed = 3
enemyspeed1 = 3
enemyspeed2 = 3
playerspeed = 2

# basestation
basestation = pygame.image.load('wood.png')

# fixed obstacles
fixedobstacle1img = pygame.image.load('trap.png')
fixedobstacle2img = pygame.image.load('volcano256.png')
fixedobstacle3img = pygame.image.load('traps.png')
fixedobstacle4img = pygame.image.load('skull2.png')
fixedobstacle01img = pygame.image.load('fire64.png')
fixedobstacle02img = pygame.image.load('toxic.png')

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10
 
def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255,255,255))
    screen.blit(score,(x, y))

def fbasestation(x, y):
    screen.blit(basestation, (x, y))


def player1(x, y):
    screen.blit(player1img, (x, y))


def enemyfor1(x, y):
    screen.blit(enemyfor1img, (x, y))


def enemyfor2(x, y):
    screen.blit(enemyfor2img, (x, y))


def enemyfor3(x, y):
    screen.blit(enemyfor3img, (x, y))


# def enemyfor4(x, y):
#     screen.blit(enemyfor4img, (x, y))
#
# def enemyfor5(x, y):
#     screen.blit(enemyfor5img, (x, y))

def enemyfor11(x, y):
    screen.blit(enemyfor2img, (x, y))


def enemyfor21(x, y):
    screen.blit(enemyfor5img, (x, y))


def enemyfor31(x, y):
    screen.blit(enemyfor4img, (x, y))


# def enemyfor41(x, y):
#     screen.blit(enemyfor3img, (x, y))
#
# def enemyfor51(x, y):
#     screen.blit(enemyfor1img, (x, y))

def fixedobstacle1(x, y):
    screen.blit(fixedobstacle1img, (x, y))


def fixedobstacle2(x, y):
    screen.blit(fixedobstacle2img, (x, y))


def fixedobstacle3(x, y):
    screen.blit(fixedobstacle3img, (x, y))


def fixedobastacle4(x, y):
    screen.blit(fixedobstacle4img, (x, y))


def fixedobstacle01(x, y):
    screen.blit(fixedobstacle01img, (x, y))


def fixedobstacle02(x, y):
    screen.blit(fixedobstacle02img, (x, y))


def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - player1Y, 2)))
    if distance < 60:
        return True
    else:
        return False

def isCollisiono(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - player1Y, 2)))
    if distance < 96:
        return True
    else:
        return False


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
                player1X_change = -playerspeed
            if event.key == pygame.K_RIGHT:
                player1X_change = playerspeed
            if event.key == pygame.K_UP:
                player1Y_change = -playerspeed
            if event.key == pygame.K_DOWN:
                player1Y_change = playerspeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player1X_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1Y_change = 0

    player1X += player1X_change
    player1Y += player1Y_change

    for j in range(0, 960, 45):
        i = 10
        fbasestation(j, i)
        i = 220
        fbasestation(j, i)
        i = 260
        fbasestation(j, i)
        i = 470
        fbasestation(j, i)
        i = 515
        fbasestation(j, i)
        i = 735
        fbasestation(j, i)

        # placing fixed obstacles
        fixedobstacle1(fixedobstacle1X, fixedobstacle1Y)
        fixedobstacle2(fixedobstacle2X, fixedobstacle2Y)
        fixedobstacle3(fixedobstacle3X, fixedobstacle3Y)
        fixedobstacle01(fixedobstacle01X, fixedobstacle01Y)
        fixedobstacle02(fixedobstacle02X, fixedobstacle02Y)
        fixedobastacle4(fixedobstacle4X, fixedobstacle4Y)

    # stoping the player from going out of border
    # introducing boundaries
    # beyond boundaries
    if player1X < 0 or player1X > 939:
        player1X_change = 0
    if player1Y < 0 or player1Y > 730:
        player1Y_change = 0

    # enemy follows the player

    if (player1Y > 20 and player1Y < 400):
        if player1X < enemyfor1X:
            enemyfor1X -= enemyspeed
        elif player1X > enemyfor1X:
            enemyfor1X += enemyspeed
        if player1X < enemyfor11X:
            enemyfor11X -= enemyspeed1
        elif player1X > enemyfor11X:
            enemyfor11X += enemyspeed1

    if (player1Y > c + b - 5 and player1Y < c + 4 * b):
        if player1X < enemyfor2X:
            enemyfor2X -= enemyspeed1
        elif player1X > enemyfor2X:
            enemyfor2X += enemyspeed
        if player1X < enemyfor21X:
            enemyfor21X -= enemyspeed
        elif player1X > enemyfor21X:
            enemyfor21X += enemyspeed1

    if (player1Y > c + 2 * b + 5 and player1Y < c + 5 * b):
        if player1X < enemyfor3X:
            enemyfor3X -= enemyspeed1
        elif player1X > enemyfor3X:
            enemyfor3X += enemyspeed
        if player1X < enemyfor31X:
            enemyfor31X -= enemyspeed2
        elif player1X > enemyfor31X:
            enemyfor31X += enemyspeed1

    collision1 = isCollision(enemyfor1X, enemyfor1Y, player1X, player1Y)
    collision2 = isCollision(enemyfor2X, enemyfor2Y, player1X, player1Y)
    collision3 = isCollision(enemyfor3X, enemyfor3Y, player1X, player1Y)
    collision4 = isCollision(enemyfor11X, enemyfor11Y, player1X, player1Y)
    collision5 = isCollision(enemyfor21X, enemyfor21Y, player1X, player1Y)
    collision6 = isCollision(enemyfor31X, enemyfor31Y, player1X, player1Y)
    collision7 = isCollisiono(fixedobstacle1X, fixedobstacle1Y, player1X, player1Y)
    collision8 = isCollisiono(fixedobstacle2X, fixedobstacle2Y, player1X, player1Y)
    collision9 = isCollisiono(fixedobstacle3X, fixedobstacle3Y, player1X, player1Y)
    collision10 = isCollisiono(fixedobstacle4X, fixedobstacle4Y, player1X, player1Y)
    collision11 = isCollision(fixedobstacle01X, fixedobstacle01Y, player1X, player1Y)
    collision12 = isCollision(fixedobstacle02X, fixedobstacle02Y, player1X, player1Y)

    if collision1 or collision2 or collision3 or collision4 or collision5 or collision6 or collision7 or collision8 or collision9 or collision10 or collision11 or collision12:
        #what to do when dead
        player1X = 460
        player1Y = 720
    # Game loop

    # if  (player1Y > c + 3 *b + 5 and player1Y < c + 7*b):
    #     if player1X < enemyfor4X:
    #         enemyfor4X -= enemyspeed
    #     elif player1X > enemyfor4X:
    #         enemyfor4X += enemyspeed
    #     if player1X < enemyfor41X:
    #         enemyfor41X -= enemyspeed2
    #     elif player1X > enemyfor41X:
    #         enemyfor41X += enemyspeed
    #
    # if  (player1Y > c + 4 *b and player1Y < c + 9*b):
    #     if player1X < enemyfor5X:
    #         enemyfor5X -= enemyspeed
    #     elif player1X > enemyfor5X: 
    #         enemyfor5X += enemyspeed1
    #     if player1X < enemyfor51X:
    #         enemyfor51X -= enemyspeed
    #     elif player1X > enemyfor51X:
    #         enemyfor51X += enemyspeed2

    if (player1Y > enemyfor1Y):
        score_value +=10
    if (player1Y > enemyfor11Y):
        score_value += 10
    if (player1Y > enemyfor2Y):
        score_value +=10
    if (player1Y > enemyfor21Y):
        score_value +=10
    if (player1Y > enemyfor3Y):
        score_value +=10
    if (player1Y > enemyfor31Y):
        score_value +=10

    if(player1Y > fixedobstacle1Y):
        score_value +=5
    if (player1Y > fixedobstacle2Y):
        score_value += 5
    if (player1Y > fixedobstacle3Y):
        score_value += 5
    if (player1Y > fixedobstacle4Y):
        score_value += 5
    if (player1Y == fixedobstacle01Y):
        score_value += 5
    if (player1Y == fixedobstacle02Y):
        score_value += 5


    player1(player1X, player1Y)
    enemyfor1(enemyfor1X, enemyfor1Y)
    enemyfor2(enemyfor2X, enemyfor2Y)
    enemyfor3(enemyfor3X, enemyfor3Y)
    # enemyfor4(enemyfor4X, enemyfor4Y)
    # enemyfor5(enemyfor5X, enemyfor5Y)
    enemyfor11(enemyfor11X, enemyfor11Y)
    enemyfor21(enemyfor21X, enemyfor21Y)
    enemyfor31(enemyfor31X, enemyfor31Y)
    # enemyfor41(enemyfor41X, enemyfor41Y)
    # enemyfor51(enemyfor51X, enemyfor51Y)
    show_score(textX, textY)

    pygame.display.update()
