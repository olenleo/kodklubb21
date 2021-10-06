WIDTH = 600
HEIGHT = 600

# FÄRGER - röd, grön, blå
# Skala 0-255
RED = 200,0,0
PLAYER = Rect((400, 0), (10, 10))
HASTIGHET_Y = 0

def draw():
    screen.draw.rect(PLAYER, RED)


def update():
    global HASTIGHET_Y
    screen.clear()


    if keyboard.left:
        PLAYER.x -= 1 # PLAYER.x = PLAYER.x - 1

    if keyboard.right:
        PLAYER.x += 1

    # TYNGDKRAFT
    if PLAYER.y < 500:
        HASTIGHET_Y += 0.4
        PLAYER.y += HASTIGHET_Y




