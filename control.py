
def hit_walls(snake, field):
    '''
    we check is there are any collisions between snake head and
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


def snake_move(snake, field):
    '''
    condition: next cell, in direction where snake moving should be
    cell with indexes more than 0 and less than size of field.
    basically not hit the walls.
    second condition we should not hit the tail
    if tail is not empty:
    we add at 0 position into tail current position of the head
    so all other elements will be moved by one index to the end
    and pop last element of the tail. After that
    we move head for one position into it direction
    and call transfer(snake, field) to give 

    '''
    tail = snake.tail.tail
    dy, dx = snake.directions[snake.direction]
    print(dy, dx)
    if not hit_walls(snake, field) and not hit_tail(snake):
        if tail:
            tail.insert(0, (snake.y, snake.x))
            tail.pop()
        snake.y += dy
        snake.x += dx
        transfer(snake, field)

