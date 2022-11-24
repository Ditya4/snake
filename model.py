import numpy as np
from random import randint


class Field():
    '''
    We create a game field filled with 0. 0 is going to be a black square.
    '''

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.field = self.create_field()

    def create_field(self):
        result = np.zeros(self.rows * self.columns, np.int32).reshape(
                        self.rows, self.columns)
        result[self.rows - 1] = np.ones(self.columns, np.int32)
        return result

    def __str__(self):
        return str(self.field)


class Target():

    def __init__(self, snake, field):
        '''
        snake we need for target not appear at snake head and tail
        field to get rows and columns
        _try_counter_flag count from 1 to 100 tries to find cell for target,
        if we can, we make this variable equals to 0 and while is done.
        if we hit the target of 100 we call method _check_empty - which should
        check is there any zero cell, if not any zero cell return 1(some error)
        next we generate y and x indexes and if in field.field at y, x indexes
        is zero - we put the target there
        and increase _try_counter_flag
        '''
        try_counter_flag = 1
        while try_counter_flag:
            try_counter_flag += 1
            if try_counter_flag >= 100:
                is_empty = self.check_empty(field)
                if not is_empty:
                    self.created = False
                    try_counter_flag = 0
            y_index = randint(0, field.rows - 1)
            x_index = randint(0, field.columns - 1)
            if not field.field[y_index][x_index]:
                self.y = y_index
                self.x = x_index
                self.created = True
                try_counter_flag = 0


















    def _check_empty(self, field):
        '''
        we check is there any zero cell. if so - return True else return False
        '''
        for y in range(field.rows):
            for x in range(field.columns):
                if not field.field[y][x]:
                    return True
        return False










class Tail():

    def __init__(self):
        self.tail = []

    def add(self, y, x):
        self.tail.append([y, x])

    def draw(self, field):
        for y, x in self.tail:
            field.field[y][x] = 1


class Snake():

    def __init__(self, y, x, direction):
        '''
        y, x are indexes of row and column of head of the snake
        tail is going to be a class of snake tail
        directions is going to be a dict with pairs of dy and dx
        indexes change
        '''
        self.y = y
        self.x = x
        self.direction = direction
        self.tail = Tail()
        # next lines is test line
        
        self.tail.add(y - 1, x)
        self.tail.add(y - 2, x)
        self.tail.add(y - 3, x)
        self.tail.add(y - 4, x)
        self.tail.add(y - 5, x)
        
        self.directions = {"left": (0, -1),
                           "right": (0, 1),
                           "up": (-1, 0),
                           "down": (1, 0),
                           }


if __name__ == "__main__":
    rows = 15
    columns = 15
    start_y = 5
    start_x = 5
    right = "right"

    field = Field(rows, columns)
    print(field)
    snake = Snake(start_y, start_x, right)
