from game_state import GameState
from grid import Grid
from piece import Piece
import pygame
import random
from shapes import SHAPES
from gravity import Gravity
from game_view import GameView

class Game:
    def __init__(self):
        self.state = self.get_initial_state()
        self.view = GameView()

    def get_random_shape_id(self):
        return random.randint(0, len(SHAPES) - 1)

    def get_initial_state(self):
        return GameState(
            grid=Grid(),
            piece=Piece(self.get_random_shape_id()),
            gravity=Gravity(),
            next_shape_id=self.get_random_shape_id()
        )

    def move_piece(self, move_x, move_y):
        piece = self.state.piece

        can_move = self.state.grid.can_fit_shape(piece.shape, piece.x + move_x, piece.y + move_y)

        if can_move:
            piece.move(move_x, move_y)
        return can_move

    def rotate_piece(self):
        piece = self.state.piece

        new_shape = piece.rotate()
        can_rotate = self.state.grid.can_fit_shape(new_shape, piece.x, piece.y)

        if can_rotate:
            piece.shape = new_shape
        return can_rotate

    def handle_piece_landing(self):
        state = self.state
        state.grid.lock_piece(state.piece)

        cleared_lines = state.grid.clear_compute_lines()
        state.score += cleared_lines

        new_piece = Piece(state.next_shape_id)

        if state.grid.can_fit_shape(new_piece.shape, new_piece.x, new_piece.y):
            state.piece = new_piece
            state.next_shape_id = self.get_random_shape_id()
        else:
            state.is_game_over = True

    def move_piece_down(self):
        self.state.gravity.reset_progress()

        did_move = self.move_piece(0, 1)
        if not did_move:
            self.handle_piece_landing()

        return did_move

    def update(self, inputs, dt):
        if self.state.is_game_over:
            if pygame.K_r in inputs:
                self.state = self.get_initial_state()
            return

        if pygame.K_LEFT in inputs:
            self.move_piece(-1, 0)

        if pygame.K_RIGHT in inputs:
            self.move_piece(1, 0)

        if pygame.K_UP in inputs:
            self.rotate_piece()

        if pygame.K_DOWN in inputs:
            self.move_piece_down()

        if pygame.K_SPACE in inputs:
            while self.move_piece_down():
                pass

        should_drop = self.state.gravity.update_progress(dt)
        if should_drop:
            self.move_piece_down()


    def start(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        pygame.key.set_repeat(400, 10)
        clock = pygame.time.Clock()

        self.view.init_display()

        inputs = set()

        is_running = True
        while is_running:
            dt = clock.tick(60)

            inputs.clear()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    inputs.add(event.key)
            self.update(inputs, dt)

            self.view.render(self.state)

        pygame.quit()