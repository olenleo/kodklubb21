WIDTH = 600
HEIGHT = 600
MARK = 500
# Vi sparar några färger - röd, grön, blå
# Skala 0-255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

# Skapa en actor
# Actor("filnamn", position)
# OBS!
# Filen måste finnas i mappen /images


#github.com/olenleo/kodklubb21

PLAYER = Actor("haffelix2",(20,20))
HASTIGHET_Y = 0
HASTIGHET_X = 0
GRAVITY = 1
ACTIVE_BLOCKS = []
# Vi sätter in information i tabellen!
for block in range(5):
    nytt_block = Actor("block_red_2x2",(block * 30 + 50,10))
    ACTIVE_BLOCKS.append(nytt_block)


def draw():


    PLAYER.draw()


def update():
    global HASTIGHET_Y, HASTIGHET_X, ACTIVE_BLOCKS

    screen.clear()

    for block in ACTIVE_BLOCKS:
        block.y += 1
        block.draw()


    if keyboard.left and HASTIGHET_X > -20:
        HASTIGHET_X -= 2

    if keyboard.right and HASTIGHET_X < 20:
        HASTIGHET_X += 2

    if keyboard.up:
        HASTIGHET_Y = -10



    # TYNGDKRAFT
    if PLAYER.y > MARK:
        HASTIGHET_Y = 0
        PLAYER.y = MARK

    PLAYER.y += HASTIGHET_Y
    PLAYER.x += HASTIGHET_X
    HASTIGHET_Y += GRAVITY


    if HASTIGHET_X > 0:
        HASTIGHET_X -= 1
    if HASTIGHET_X < 0:
        HASTIGHET_X += 1