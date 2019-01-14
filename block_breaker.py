import time
import pygame as pg
import random
import math
from paddle import Paddle
from ball import Ball 


pg.init()

display_width = 600
display_height = 500

# color definitionsa
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
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

def isAtBoundary(rect):
  if rect.x + rect.size[0] >= display_width:
    return True
  elif rect.x <= 0 or rect.y <= 0:
    return True
  else:
    return False

def getAngleFromPaddle(xIntersection):
  if xIntersection < 10:
    return 3.5
  else:
    rounded = round(xIntersection/10)
    speed = baseSpeed + abs(baseSpeed - rounded)
    return ((3.5 + (rounded * degrees_offset)), (speed))

def getAngle(currentAngle,rectY):
  if rectY <= 0:
    newAngle = math.pi - abs(math.pi - currentAngle)
  elif math.pi - currentAngle < 0:
    newAngle = (2*math.pi) + (math.pi - currentAngle )
  else:
    newAngle = math.pi - currentAngle
  return newAngle

speed = baseSpeed
def game_loop():
  gameDisplay.fill(pink)
  pg.display.update()
  gameExit= False
  ballOnPaddle = True
  lastBallPosition = [(0,0), (ball.rect.x, ball.rect.y)]
  while not gameExit:
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
    if  keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
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
      # get x coordinate of ball --> 
      # x coordiante of ball - paddle.x will give us where ball hit 
      # determine angle based on where ball hit
      x_offset = (ball.rect.x + 10 - paddle.rect.x)
      (angle, speed) = getAngleFromPaddle(x_offset)

    paddle_group.draw(gameDisplay)
    if ballOnPaddle:
      ball.moveBallOnPaddle((paddle.rect[0] + 48, paddle.rect[1] - 18))
    else:
      ball.update((angle, speed))
  
    if isAtBoundary(ball.rect):
      # angle = getAngle(lastBallPosition, [ball.rect.x, ball.rect.y])
      angle = getAngle(angle, ball.rect.y)


   
    # print(x_offset, y_offset)
   
    # collided = pg.sprite.spritecollide(paddle, ball_group, False)
    ball_group.draw(gameDisplay)

    dirty_rects.append(paddle.rect) 
    dirty_rects.append(ball.rect) 

    pg.display.update(dirty_rects)

    # paddle_sprite_group.update()
  
    
    clock.tick(60)
game_loop()
pg.quit()
quit()