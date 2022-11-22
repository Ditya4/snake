import numpy as np


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
        self.directions = {"left": (0, -1),
                           "right": (0, 1),
                           "up": (-1, 0),
                           "down": (1, 0),
                           }

    def move(self):
        # self.
        pass


if __name__ == "__main__":
    rows = 15
    columns = 15
    start_y = 5
    start_x = 5
    right = "right"

    field = Field(rows, columns)
    print(field)
    snake = Snake(start_y, start_x, right)
