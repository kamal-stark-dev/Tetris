from grid import Grid
from piece import Piece
from gravity import Gravity

class GameState:
    def __init__(self, grid: Grid, piece: Piece, gravity: Gravity, next_shape_id: int):
        self.is_game_over = False
        self.score = 0

        self.grid = grid
        self.piece = piece
        self.gravity = gravity
        self.next_shape_id = next_shape_id