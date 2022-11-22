from model import Snake, Field
from view import Render


rows = 15
columns = 15
size = 40

field = Field(rows, columns)

render = Render(rows, columns, size)
render.draw_field(field.field)
input()

