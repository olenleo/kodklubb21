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
collidePlatform = False
collideWall = False
haffelixHoppar = False
#-----------------------------------#

####################################
# Skapa blocks för testbruk
for block in range(3):
    nyttBlock = Actor("block_red_2x2", (block * 30 + 50, 500), anchor = ('center','bottom'))
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
    if collidePlatformCheck():
        hastighetY = 0
    if collideWallCheck():
        hastighetX = 0
    if keyboard.left and hastighetX > -8:
        if (PLAYER.x > 40):
            hastighetX -= 2
        

    if keyboard.right and hastighetX < 8:
        if (PLAYER.x < WIDTH - 40):
            hastighetX += 2

    if keyboard.up and collidePlatformCheck():
        haffelixHoppar = True
        hastighetY -= 15
        if haffelixHoppar and hastighetY < 0:
            haffelixHoppar = False

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

def collidePlatformCheck():
    collidePlatform = False
    if PLAYER.y == mark:
        collidePlatform = True
        return collidePlatform
    for block in finishedBlocks:
        if PLAYER.colliderect(block): #and collideWallCheck():
            collidePlatform = True
            PLAYER.y = block.top + 1
    return collidePlatform
    
      
def collideWallCheck():
    collideWall = False
    if PLAYER.x < 50 or PLAYER.x > WIDTH - 50:
        collideWall = True
        return collideWall
    for block in finishedBlocks:
        if PLAYER.colliderect(block) :
            print("BOOM")
            collideWall = True
            return collideWall
        
  
