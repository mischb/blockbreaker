import time
import pygame as pg
import random
import math
from paddle import Paddle
from ball import Ball
from blocks import Block


pg.init()

display_width = 600
display_height = 500

# color definitionsa
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
pink = (173, 145, 160)

gameDisplay = pg.display.set_mode((display_width, display_height))

pg.display.set_caption('break blocks')
clock = pg.time.Clock()

paddle_group = pg.sprite.GroupSingle()
paddle = Paddle(black, 100, 8)
paddle.rect.x = 20
paddle.rect.y = display_height - 45
paddle_group.add(paddle)

baseSpeed = 5
ball_group = pg.sprite.GroupSingle()
ball = Ball(paddle.rect)
ball_group.add(ball)
degrees_offset = 0.242478
dirty_rects = []

# color, length, height, position, width
block_group = pg.sprite.Group()
blocks = 20
x = 0
y = 100

# while blocks > 0:
#     new_block = Block(black, 20, 10)
#     new_block.rect.x = x
#     new_block.rect.y = y
#     block_group.add(new_block)
#     x += 32
#     blocks -= 1


def isAtBoundary(rect):
    if rect.x + rect.size[0] >= display_width:
        return True
    elif rect.x <= 0 or rect.y <= 0:
        return True
    else:
        return False


def getAngleFromPaddle(xIntersection):
    if xIntersection < 10:
        speed = baseSpeed + 5
        return (3.5, speed)
    else:
        rounded = round(xIntersection/10)
        speed = baseSpeed + abs(baseSpeed - rounded)
    return ((3.5 + (rounded * degrees_offset)), (speed))


# if d+l (radian = 270° × π/180 )
""" 
'360' = 2*math.pi
'270' = math.pi + (math.pi/2)
'180' = math.pi
 '90' = math.pi/2


if currentAngle > '270':
    if collision === right:
        newAngle = '270' - (currentAngle-270)
    elif(collision === bottom):
        newAngle = 360 - currentAngle
if currentAngle < 90 and currentAngle < 180:
    if rect.x <= 0:
        90 - (currentAngle - 90)
    elif rect.y <= 0:º
        newAngle 360-currentAngle
if 270 < currentAngle and currentAngle < 180:
    if collision === right:
            newAngle = 180 + (360 - angle)
    if collision === top
        newAngle = 360-(angle)
if 90>currentAngle:
    if collision == left:
        newAngle = 180+ (360-angle)
    else:
        newAngle = 180-(angle)

 """

'360' = 2*math.pi
'270' = math.pi + (math.pi/2)
'180' = math.pi
'90' = math.pi/2


def getAngle(currentAngle, rectY):
    if rectY <= 0:
        print(currentAngle)
        newAngle = math.pi - abs(math.pi - currentAngle)
        # newAngle = currentAngle *-1
        print(newAngle)
    elif math.pi - currentAngle < 0:
        newAngle = (2*math.pi) + (math.pi - currentAngle)
    else:
        newAngle = math.pi - currentAngle
    return newAngle


speed = baseSpeed


def game_loop():
    gameDisplay.fill(pink)
    pg.display.update()
    gameExit = False
    ballOnPaddle = True
    lastBallPosition = [(0, 0), (ball.rect.x, ball.rect.y)]
    block_group.draw(gameDisplay)
    while not gameExit:
        ballOnPaddlePosition = (paddle.rect[0] + 48, paddle.rect[1] - 18)
        lastBallPosition.pop(0)
        lastBallPosition.append((ball.rect.x, ball.rect.y))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameExit = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    gameExit = True

                if event.key == pg.K_SPACE:
                    ballOnPaddle = False

        # move paddle
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
            currentPaddleLoc = paddle.rect
            pg.draw.rect(gameDisplay, pink, currentPaddleLoc)
            dirty_rects.append(currentPaddleLoc)
            if keys[pg.K_LEFT] and paddle.rect[0] > 0:
                paddle.move_left()
            if keys[pg.K_RIGHT] and paddle.rect[0] < (display_width-100):
                paddle.move_right()

        pg.draw.rect(gameDisplay, pink, ball.rect)
        overlapped = pg.sprite.spritecollide(ball, paddle_group, False)
        if overlapped:
            x_offset = (ball.rect.x + 10 - paddle.rect.x)
            (angle, speed) = getAngleFromPaddle(x_offset)
        paddle_group.draw(gameDisplay)

        if ballOnPaddle:
            ball.moveBallOnPaddle(ballOnPaddlePosition)
        elif ball.rect.y > display_height:
            ballOnPaddle = True
            ball.moveBallOnPaddle(ballOnPaddlePosition)
        else:
            ball.update((angle, speed))

        if isAtBoundary(ball.rect):

            angle = getAngle(angle, ball.rect.y)

        # logic for removing block from screen
        hitBlock = pg.sprite.spritecollide(ball, block_group, True)
        if hitBlock:

            angle = getAngle(angle, 0)
            # draw over sprite ? get location of sprite
            for block in hitBlock:
                pg.draw.rect(gameDisplay, pink, block.rect)

                # --> draw pink over rect

        ball_group.draw(gameDisplay)

        dirty_rects.append(paddle.rect)
        dirty_rects.append(ball.rect)

        pg.display.update(dirty_rects)

        # paddle_sprite_group.update()

        clock.tick(60)


game_loop()
pg.quit()
quit()
