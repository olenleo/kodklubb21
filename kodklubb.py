#####################################
# Random behövs inte i så många program, därför är det inte alltid med.
# Med 'import' bjuder vi med andra bibliotek.
import random

# random-biblioteket behövs för slumpmåssiga tal!
# användning:
# slumpmassig_siffra = random.randint(0,10)
###################################
# Nyttiga variabler
WIDTH = 600
HEIGHT = 600
mark = 600
#-----------------------------------#

###################################
#Vi sparar några färger - röd, grön, blå
# Skala 0-255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
#-----------------------------------#

PLAYER = Actor("haffelix2", (300, 10), anchor = ('center', 'bottom'))

##############################
# OBS - globala variabler!
# Förlåt... men sånt är det med Python :S
hastighetY = 0
hastighetX = 0
gravity = 1
activeBlocks = []
finishedBlocks = []
blockIsReadyToDrop = True

#-----------------------------------#

####################################
# Skapa blocks för testbruk
for block in range(3):
    nyttBlock = Actor("block_red_2x2", (block * 30 + 50, 400), anchor = ('center','bottom'))
    activeBlocks.append(nyttBlock)
for block in range(3):
    nyttBlock = Actor("block_red_2x2", (block * 30 + 80, 250), anchor = ('center','bottom'))
    activeBlocks.append(nyttBlock)
#-----------------------------------#a




def draw():
    screen.blit("bg4", (0, 0))
    PLAYER.draw()
    for block in activeBlocks:
        block.draw()
    for block in finishedBlocks:
        block.image = 'block_blue_2x2'
        block.draw()


def update():
    global hastighetX, hastighetY, activeBlocks, finishedBlocks, blockIsReadyToDrop, readyToJump

    screen.clear()
    for block in finishedBlocks:
        if block.colliderect(PLAYER):
            PLAYER.y = block.top
            hastighetY = 1

    for block in activeBlocks:
        if block.collidelist(finishedBlocks) > -1:
            finishedBlocks.append(block)
            activeBlocks.remove(block)

    if blockIsReadyToDrop:
        blockIsReadyToDrop = False
        dropABlock()
        clock.schedule(setBlockReadyToDrop,1)

    for block in activeBlocks:
        if block.y < mark:
            block.y += 1
        else:
            finishedBlocks.append(block)
            activeBlocks.remove(block)


    ####################################
    # Spelarens rörelse

    if keyboard.left and hastighetX > -20:
        hastighetX -= 2

    if keyboard.right and hastighetX < 20:
        hastighetX += 2

    if keyboard.up and hastighetY == 1:
        hastighetY -= 10

    #-----------------------------------#


    ###############################******
    # TYNGDKRAFT
    if PLAYER.y > mark:
        hastighetY = 0
        PLAYER.y = mark

    PLAYER.y += hastighetY
    PLAYER.x += hastighetX
    hastighetY += gravity

    if hastighetX > 0:
        hastighetX -= 1
    if hastighetX < 0:
        hastighetX += 1



    #-----------------------------------#

####################################
# Här fäller vi block!
def setBlockReadyToDrop():
    global blockIsReadyToDrop
    blockIsReadyToDrop = True

def dropABlock():
    x = random.randint(1, 20) * 30
    nyttBlock = Actor("block_red_2x2", (x, -10), anchor = ('center','bottom'))
    activeBlocks.append(nyttBlock)
#-----------------------------------#
