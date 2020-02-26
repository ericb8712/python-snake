
##Made with PyGame

import pygame
import sys
import time
import random

pygame.init()

##Speed
difficulty = 12

# Window size
frame_size_x = 720
frame_size_y = 480

# Initialise game window
pygame.display.set_caption('Snek NOT Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 50)
green = (0, 180, 90)
blue = (0, 100, 200)

# FPS controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [200, 100]
snake_body = [[200, 100], [200-20, 100], [200-(2*20), 100]]

food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Hesch Verkackt', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Pünkt : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 20
    if direction == 'DOWN':
        snake_pos[1] += 20
    if direction == 'LEFT':
        snake_pos[0] -= 20
    if direction == 'RIGHT':
        snake_pos[0] += 20

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//20)) * 20, random.randrange(1, (frame_size_y//20)) * 20]
    food_spawn = True

    # Graphic
    game_window.fill(yellow)
    for pos in snake_body:
        # Snake body

        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 20, 20))

    # Snake food
    pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 20, 20))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, black, 'consolas', 30)
    # Refresh game screen
    pygame.display.update()
    fps_controller.tick(difficulty)


pygame.quit()
quit()



