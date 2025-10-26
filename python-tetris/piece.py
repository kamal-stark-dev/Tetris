import random
from config import GRID_COLS
from shapes import SHAPES

class Piece:
    def __init__(self, shape_id):
        self.shape_id = shape_id
        self.shape = SHAPES[shape_id]
        self.x = random.randint(0, GRID_COLS - len(self.shape[0]))
        self.y = 0

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def rotate(self):
        rows = len(self.shape)
        cols = len(self.shape[0])

        return [[self.shape[rows - 1 - i][j] for i in range(rows)] for j in range(cols)]
