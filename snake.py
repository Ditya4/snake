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
control.transfer(snake, field)
start = time()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # next line need to send into control
    if time() - start > delta_t:
        control.snake_move(snake, field)
        start = time()

    control.snake_move(snake, field)
    render.draw_field(field.field)

    pygame.time.delay(fps)

pygame.quit()
