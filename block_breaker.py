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

speed = 15
ball_group = pg.sprite.GroupSingle()
ball = Ball(paddle.rect)
ball_group.add(ball)

dirty_rects = []

  
#     gameDisplay.blit(ball.image, (paddleRect[0] + 48,paddleRect[1] - 18))
    
def game_loop():
  gameDisplay.fill(pink)
  pg.display.update()
  gameExit= False
  ballOnPaddle = True
  while not gameExit:
    
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

    paddle_group.draw(gameDisplay)
    if ballOnPaddle:
      ball.moveBallOnPaddle((paddle.rect[0] + 48, paddle.rect[1] - 18))
    else:
      ball.update((6.2831853072, speed))

    collided = pg.sprite.spritecollide(paddle, ball_group, False)

    print(collided)

    ball_group.draw(gameDisplay)

    dirty_rects.append(paddle.rect) 
    dirty_rects.append(ball.rect) 

    pg.display.update(dirty_rects)

    # paddle_sprite_group.update()
  
    
    clock.tick(60)
game_loop()
pg.quit()
quit()