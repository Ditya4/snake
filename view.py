import pygame


class Render():
    '''
    Draw squares on canvas  for every not zero table object,
    all zeros fill with black color.
    We have an array for our game field, filled with integer values,
    every value is a number which is equivalent to color.
    0 - black
    1 - white (snake tail)
    2 - green (snake head)
    3 - red (target) or maybe we make it like a target.gif
    '''

    def __init__(self, rows, columns, size):
        self.rows = rows
        self.columns = columns
        self.size = size
        self.canvas = self.create_canvas()
        pygame.init()
        self.colors_decode = {0: "black",
                              1: "white",
                              2: "green",
                              3: "red",
                              }

    def create_canvas(self):
        window_height = self.size * self.rows
        window_width = self.size * self.columns
        canvas = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Python")
        return canvas

    def __call__(self, field):
        self.draw_field(field)

    def draw_field(self, field):
        self.canvas.fill((0, 0, 0))
        for i in range(self.rows):
                for j in range(self.columns):
                    if field[i][j]:
                        '''
                        print(i * self.size,
                              j * self.size,
                              field[i][j],
                              self.colors_decode[
                                  firld[i][j]])
                        '''
                        pygame.draw.rect(
                            self.canvas,
                            self.colors_decode[field[i][j]],
                            (j * self.size, i * self.size,
                             self.size, self.size))
                        pygame.draw.rect(
                            self.canvas,
                            self.colors_decode[0],
                            (j * self.size, i * self.size,
                             self.size, self.size), 1)
        pygame.display.update()


if __name__ == "__main__":
    rows = 15
    columns = 11
    size = 40

    canvas = Render(rows, columns, size)
    input()
