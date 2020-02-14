 ## This is a snake like game
 ## it is called snek for dank reasons
 ## this was written by eric
 ## it wasn't actually written by eric, but rather by rocco Ciccone

import pygame
import time
import random

from pygame import (init as init,
                    QUIT as pquit,
                    KEYDOWN as keydown,
                    K_LEFT as k_left,
                    K_RIGHT as k_right,
                    K_UP as k_up,
                    K_DOWN as k_down,
                    K_q as k_q,
                    K_c as k_c)
from pygame.display import (set_mode as set_mode,
                            update,
                            set_caption)
from pygame.event import (get as get_event)
from pygame.draw import (rect as color)
from pygame.font import (SysFont as font)
from pygame.time import (Clock as clock)


init()

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

dis_width = 500
dis_height = 450

dis = set_mode((dis_width, dis_height))
set_caption("snek NOT snake")

clock = clock()

snake_block = 10
snake_speed = 25

font_style = font(None, 50)

def message (msg, color):
    mesg = font_style.render (msg, True, color)
    dis.blit (mesg, [dis_width/4, dis_height/3])

def gameLoop():
    game_over = False
    game_close = False

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

while not game_over:

    while game_close == True:
        dis.fill(white)
        message("Du hesch verkackt! Druck Q zum leave oder C zum nomal spiele")
        update()

        for event in get_event():

            if event.type == keydown:

                if event.key == k_q:
                    game_over = True
                    game_close = False
                
                if event.key == k_c:
                    gameLoop()

        for event in get_event():
            if event.type == pquit:
                game_over = True

            if event.type == keydown:

                if event.key == k_left:
                    x1_change = -snake_block
                    y1_change = 0

                elif event.key == k_right:
                    x1_change = snake_block
                    y1_change = 0

                elif event.key == k_up:
                    y1_change = -snake_block
                    x1_change = 0

                elif event.key == k_down:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        color(dis, red, [foodx, foody, snake_block, snake_block])
        color(dis, blue, [x1, y1, snake_block, snake_block])
        update()

        if x1 == foodx and y1 == foody:
            print ("mmmhhhh läcka")
        clock.tick(snake_speed)

    pquit()
    quit()

gameLoop()

