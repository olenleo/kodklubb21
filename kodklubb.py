#####################################
# Till exempel random behövs inte i så många program, därför är det inte alltid med.
# Med 'import' bjuder vi med andra bibliotek.
import random

###################################
# Viktiga variabler
WIDTH = 600
HEIGHT = 600

#-----------------------------------#

###################################
# Vi sparar några färger - röd, grön, blå
# Skala 0-255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
#-----------------------------------#

##############################
# OBS - dessa är *globala* variabler!
# global hastighetX
# Förlåt... men sånt är livet!
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
#-----------------------------------#


####################################
# draw()-loopen körs varje gång pygame ritar något

def draw():
    screen.blit("bg4", (0, 0))
    PLAYER.draw()
    for block in activeBlocks:
        block.draw()
    for block in finishedBlocks:
        # vad händer här?
        print("Vad händer här?")
#-----------------------------------#

####################################
# update()-loopen körs hela tiden :)
# kom ihåg indentationen - den visar var funktionen slutar!

def update():
    global hastighetX, hastighetY, activeBlocks, finishedBlocks, blockIsReadyToDrop, readyToJump
#### <--- indentation
    screen.clear()

    if blockIsReadyToDrop:
        # Nästa block är inte färdigt ännu!
        # Metod för att fälla block?
        clock.schedule(metod, 1) # Vilken metod förbereder nästa block?

    for block in activeBlocks:
        if block.y < mark:
            block.y += 1
        else:
            finishedBlocks.append(block)
            activeBlocks.remove(block)


    ####################################
    # Spelarens rörelse

#### vi är ännu i update()...
    if keyboard.left and hastighetX > -20:
        hastighetX -= 2

    if keyboard.right and hastighetX < 20:
        hastighetX += 2

    if keyboard.up and hastighetY == 1:
        hastighetY -= 15

    #-----------------------------------#


    ###############################******
    # TYNGDKRAFT
    if PLAYER.y >= mark:
        hastighetY = 0
        PLAYER.y = mark

    PLAYER.y += hastighetY
    PLAYER.x += hastighetX
    hastighetY += gravity
#### vi är ännu i update()...
    if hastighetX > 0:
        hastighetX -= 1
    if hastighetX < 0:
        hastighetX += 1


# men HÄR slutar update()
#-----------------------------------#


####################################
# Här fäller vi block!
def setBlockReadyToDrop():
    global blockIsReadyToDrop
    # True eller False?

def dropABlock():
    x = 10 # gör x till en slumpmässig siffra!
    nyttBlock = Actor("block_red_2x2", (x, -10), anchor = ('center','bottom'))
    # nu har vi ett nytt block... hur sparar vi den i minnet?
#-----------------------------------#