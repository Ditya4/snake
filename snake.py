import pygame
from time import time
from sys import exit
from model import Snake, Field, Target
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
target_color_id = 3
count_targets = 3
render = Render(rows, columns, size)
field = Field(rows, columns)
snake = Snake(start_y, start_x, right)
targets = []
control.fill_field(snake, field)
for i in range(count_targets):
    targets.append(Target(snake, field))

if targets:
    for target in targets:
        if not target.created:
            print("Can't create target. Probably all cells are occupied.")
            exit()
        field.field[target.y][target.x] = target_color_id

# control.add_target(targets[0], field)
start = time()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if time() - start > delta_t:
        control.snake_move(snake, field, targets)
        start = time()

    for i in range(count_targets - len(targets)):
        print(len(targets))
        # if not targets[i].created:
        #     print("Can't create target. Probably all cells are occupied.")
        #     done = False
        targets.append(Target(snake, field))

    for target in targets:
        if not target.created:
            print("Can't create target. Probably all cells are occupied.")
            exit()
        field.field[target.y][target.x] = target_color_id

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
