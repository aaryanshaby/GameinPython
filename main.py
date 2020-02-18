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


# player1 = Gondorians
player1img = pygame.image.load('player1.png')
player1X = 460
player1Y = 720
playerX = 460
playerY = 720
# player2 = Rohanians
player2img = pygame.image.load('player1.png')
player2X = 460
player2Y = 5
#rounds
rounding = 1
enemyfor1X_change = 0
enemyfor1Y_change = 0
a = 92
b = 140
c = 10
cute = 5
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

#fixed obstacles
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

score_list = [None]*6
time_score = 100
time_score_change = 0.1
player1X_change = 0
player1Y_change = 0
enemyspeed = 2
enemyspeed1 = 2
enemyspeed2 = 2
playerspeed = 5

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
font = pygame.font.Font('freesansbold.ttf', 24)

textX = 10
textY = 10

textZ = 900
textA = 10

over = pygame.font.Font('freesansbold.ttf', 24)

def show_round(x, y):
    round = font.render("Round:" + str(math.ceil(rounding/2)), True, (255, 255, 255))
    screen.blit(round, (x, y))

def show_score(x, y):
    score = font.render("Score:" + str(score_value+ math.floor(time_score)), True, (255, 255, 255))
    screen.blit(score, (x, y))


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
def resetgame():
    print("reset game called")
    global counter, cr1, cr2, cr3, cr4, cr5, cr6, cr7, cr8, cr9, cr10, cr11, cr12, time_score_change
    global score_list, score_value, time_score, time_score_change, rounding
    score_list[rounding - 1] = score_value + math.floor(time_score)
    print (score_list)
    score_value = 0
    time_score = 100
    time_score_change = 0
    rounding += 1
    counter = 0
    cr1 = 0
    cr2 = 0
    cr3 = 0
    cr4 = 0
    cr5 = 0
    cr6 = 0
    cr7 = 0
    cr8 = 0
    cr9 = 0
    cr10 = 0
    cr11 = 0
    cr12 = 0
    time_score_change = 0.1
    global player1X
    global player1Y
    global player2X
    global player2Y,enemyspeed,enemyspeed1,enemyspeed2

    print(player1X,player1Y)
    print(rounding)

    if  rounding%2==0:
        player1X = player2X
        player1Y = player2Y
        enemyspeed += 1
        enemyspeed2 += 1
        enemyspeed += 1
    else:
        player1X = playerX
        player1Y = playerY

    print(player1X,player1Y,rounding)
def gameend():
    screen.fill((0,0,0,))
    score1 = font.render( "             round1             round2",True,(255,255,255))
    screen.blit(score1,(200,200))
    for event1 in pygame.event.get():
        if event1 == pygame.K_SPACE:
            print("space os pressed")
            exit()

counter = 0
cr1 = 0
cr2 = 0
cr3 = 0
cr4 = 0
cr5 = 0
cr6 = 0
cr7 = 0
cr8 = 0
cr9 = 0
cr10 = 0
cr11 = 0
cr12 = 0

running = True
while running:
    # background color

    if rounding > 6:
        gameend()
        break

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
        # what to do when dead
        resetgame()
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

    if (((player1Y < enemyfor1Y and rounding % 2 == 1) or (player1Y + cute > enemyfor1Y and rounding % 2 == 0)) and cr1 == 0):
        counter = 1
        cr1 = 1
    if (((player1Y < enemyfor11Y and rounding % 2 == 1) or (player1Y + cute > enemyfor11Y and rounding % 2 == 0)) and cr11 == 0):
        counter = 1
        cr11 = 1
    if (((player1Y < enemyfor2Y and rounding % 2 == 1) or (player1Y + cute > enemyfor2Y and rounding % 2 == 0)) and cr3 == 0):
        counter = 1
        cr3 = 1
    if (((player1Y < enemyfor21Y and rounding % 2 == 1) or (player1Y + cute > enemyfor21Y and rounding % 2 == 0)) and cr4 == 0):
        counter = 1
        cr4 = 1
    if (((player1Y < enemyfor3Y and rounding % 2 == 1) or (player1Y + cute > enemyfor3Y and rounding % 2 == 0)) and cr2 == 0):
        counter = 1
        cr2 = 1
    if (((player1Y < enemyfor31Y and rounding % 2 == 1) or (player1Y + cute > enemyfor31Y and rounding % 2 == 0)) and cr5 == 0):
        counter = 1
        cr5 = 1
    if (((player1Y < fixedobstacle1Y and rounding % 2 == 1) or (player1Y + cute > fixedobstacle1Y and rounding % 2 == 0)) and cr6 == 0):
        counter = 1
        cr6 = 1
    if (((player1Y < fixedobstacle2Y and rounding % 2 == 1) or (player1Y + cute > fixedobstacle2Y and rounding % 2 == 0)) and cr7 == 0):
        counter = 1
        cr7 = 1
    if (((player1Y < fixedobstacle3Y and rounding % 2 == 1) or (player1Y + cute > fixedobstacle3Y and rounding % 2 == 0)) and cr8 == 0):
        counter = 1
        cr8 = 1
    if (((player1Y < fixedobstacle4Y and rounding % 2 == 1) or (player1Y + cute > fixedobstacle4Y and rounding % 2 == 0)) and cr9 == 0):
        counter = 1
        cr9 = 1
    if (((player1Y < fixedobstacle01Y and rounding % 2 == 1) or (player1Y + cute > fixedobstacle01Y and rounding % 2 == 0)) and cr10 == 0):
        counter = 2
        cr10 = 1
    if (((player1Y < fixedobstacle02Y and rounding % 2 == 1) or (player1Y + cute > fixedobstacle02Y and rounding % 2 == 0)) and cr12 == 0):
        counter = 2
        cr12 = 1
    if counter == 1:
        score_value += 10
        counter = 0
    if counter == 2:
        score_value += 5
        counter = 0
    if score_value == 90:
         resetgame()
    time_score-=time_score_change





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
    show_round(textZ, textA)
    pygame.display.update()
