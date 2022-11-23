import pygame
from time import time
from model import Snake, Field
from view import Render
import control



rows = 15
columns = 15
size = 40
fps = 20
start_y = 5
start_x = 5
left = "left"
right = "right"
up = "up"
down = "down"
delta_t = 1
render = Render(rows, columns, size)
field = Field(rows, columns)
snake = Snake(start_y, start_x, right)
control.fill_field(snake, field)
start = time()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if time() - start > delta_t:
        control.snake_move(snake, field)
        start = time()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake.direction = left

    if keys[pygame.K_RIGHT]:
        snake.direction = right

    if keys[pygame.K_UP]:
        snake.direction = up

    if keys[pygame.K_DOWN]:
        snake.direction = down

    render.draw_field(field.field)

    pygame.time.delay(fps)

pygame.quit()
