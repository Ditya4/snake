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


class Snake():

    def __init__(self):
        pass


if __name__ == "__main__":
    rows = 15
    columns = 15

    field = Field(rows, columns)
    print(field)