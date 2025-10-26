from config import GRID_ROWS, GRID_COLS

EMPTY_BLOCK = -1

class Grid:
    def __init__(self):
        self.matrix = [[EMPTY_BLOCK] * GRID_COLS for _ in range(GRID_ROWS)]

    def can_fit_shape(self, shape, x, y):
        for i, row in enumerate(shape):
            for j, is_solid in enumerate(row):
                if not is_solid:
                    continue
                grid_x, grid_y = x + j, y + i

                # wall collision
                if grid_x < 0 or grid_x >= GRID_COLS:
                    return False

                # floor collision
                if grid_y >= GRID_ROWS:
                    return False

                if self.matrix[grid_y][grid_x] != EMPTY_BLOCK:
                    return False

        return True

    def lock_piece(self, piece):
        for i, row in enumerate(piece.shape):
            for j, is_solid in enumerate(row):
                if is_solid:
                    self.matrix[i + piece.y][j + piece.x] = piece.shape_id

    def clear_compute_lines(self):
        cleared_lines = 0

        for i in reversed(range(len(self.matrix))):
            if all(block != EMPTY_BLOCK for block in self.matrix[i]):
                cleared_lines += 1
            elif cleared_lines > 0:
                self.matrix[i + cleared_lines] = self.matrix[i][:]

        for i in range(cleared_lines):
            self.matrix[i] = [EMPTY_BLOCK] * GRID_COLS

        return cleared_lines
