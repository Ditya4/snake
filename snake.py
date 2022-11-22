import pygame
from model import Snake, Field
from view import Render



rows = 15
columns = 15
size = 40
time_delay = 20
start_y = 5
start_x = 5
left = "left"
right = "right"
up = "up"
down = "down"
render = Render(rows, columns, size)
field = Field(rows, columns)
snake = Snake(start_y, start_x, right)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # next line need to send into control
    snake.move()
    render.draw_field(field.field)

    pygame.time.delay(time_delay)

pygame.quit()
