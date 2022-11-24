
def add_target(target, field):
    field.field[target.y][target.x] = 3


def hit_borders(snake, field):
    '''
    we check is there going to be any collisions between snake head and
    walls at the next snake move
    '''
    y = snake.y
    x = snake.x
    dy, dx = snake.directions[snake.direction]
    if 0 <= y + dy < field.rows and 0 <= x + dx < field.columns:
        return False
    else:
        return True


def hit_tail(snake):
    '''
    if tail is empty we could move in any direction and cause we check
    not hitting the walls in another function with and condition so
    here just check tail
    if tail is not empty - we check is the next cell, in which head is
    going to move is inside tail list but not the last in tail list
    cause last is going to pop from tail list
    '''
    tail = snake.tail.tail
    if not tail:
        return False

    y = snake.y
    x = snake.x
    dy, dx = snake.directions[snake.direction]

    if (y + dy, x + dx) in tail[: -1]:
        return True
    else:
        return False


def fill_field(snake, field):
    '''
    filled snake head position on field wiht color index 2, and all tail cells
    with color index 1
    '''
    field.field[snake.y][snake.x] = 2

    for pos_y, pos_x in snake.tail.tail:
        field.field[pos_y][pos_x] = 1


def erase_old_snake_with_new_tail(snake, field):
    '''
    we erase position of head and all elements of tail
    '''
    field.field[snake.y][snake.x] = 0
    for y, x in snake.tail.tail:
        field.field[y][x] = 0


def snake_move(snake, field):
    '''
    condition: next cell, in direction where snake moving should be
    cell with indexes more than 0 and less than size of field.
    basically not hit the walls.
    second condition we should not hit the tail
    if tail is not empty:
    we add at 0 position into tail current position of the head
    so all other elements will be moved by one index to the end,
    pop last element of the tail and erase this poped element from field.
    After that we erase old snake from the field(remembering, what last element
    of the tail was previously erased),
    we move head for one position into it direction
    and call fill_field(snake, field) to fill field with new snake position.

    '''
    tail = snake.tail.tail
    dy, dx = snake.directions[snake.direction]
    # print(dy, dx)
    if not hit_borders(snake, field) and not hit_tail(snake):
        if tail:
            tail.insert(0, (snake.y, snake.x))
            erase_y, erase_x = tail.pop()
            field.field[erase_y][erase_x] = 0
        erase_old_snake_with_new_tail(snake, field)
        snake.y += dy
        snake.x += dx
        fill_field(snake, field)
