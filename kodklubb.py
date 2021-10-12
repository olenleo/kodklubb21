WIDTH = 600
HEIGHT = 600
MARK = 500
# FÄRGER - röd, grön, blå
# Skala 0-255
RED = 200,0,0
PLAYER = Rect((400, 0), (10, 10))
HASTIGHET_Y = 0
HASTIGHET_X = 0
GRAVITY = 1

def draw():
    screen.draw.filled_rect(PLAYER, RED)


def update():
    global HASTIGHET_Y
    screen.clear()

    if keyboard.left:
        PLAYER.x -= 1

    if keyboard.right:
        PLAYER.x += 1

    if keyboard.up:
        HASTIGHET_Y = -20


    # TYNGDKRAFT
    if PLAYER.y > MARK:
        HASTIGHET_Y = 0
        PLAYER.y = MARK

    PLAYER.y += HASTIGHET_Y
    HASTIGHET_Y += GRAVITY
    #if HASTIGHET_Y > 2 or HASTIGHET_Y < -2:
    #    print(HASTIGHET_Y)
    screen.draw.filled_rect(PLAYER, RED)

