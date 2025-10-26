from game_state import GameState
from config import (ALPHA_GAME_OVER_OVERLAY, BLOCK_SIZE, COLOR_BACKGROUND, COLOR_EMPTY_BLOCK,
    COLOR_FONT, COLOR_GAME_OVER_OVERLAY, COLOR_SIDEBAR_BORDER, GRID_COLS, GRID_ROWS, SHAPE_COLORS,
    SIDEBAR_BORDER, SIDEBAR_WIDTH_BLOCKS)
import pygame
from shapes import SHAPES
from grid import EMPTY_BLOCK

GRID_WIDTH = GRID_COLS * BLOCK_SIZE
GRID_HEIGHT = GRID_ROWS * BLOCK_SIZE

SIDEBAR_WIDTH = SIDEBAR_WIDTH_BLOCKS * BLOCK_SIZE
SIDEBAR_CONTEXT_X = GRID_WIDTH + SIDEBAR_BORDER + BLOCK_SIZE
SIDEBAR_CONTEXT_Y = BLOCK_SIZE

GAME_WIDTH = GRID_WIDTH + SIDEBAR_BORDER + SIDEBAR_WIDTH
GAME_HEIGHT = GRID_HEIGHT

class GameView:
    def init_display(self):
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.font = pygame.font.SysFont("Monaco", 32, bold=True)

    def draw_block(self, color, x, y):
        self.screen.fill(color, (x, y, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

    def draw_shape(self, shape, shape_id, x, y):
        for i, row in enumerate(shape):
            for j, is_solid in enumerate(row):
                if is_solid:
                    self.draw_block(SHAPE_COLORS[shape_id], x + j * BLOCK_SIZE, y + i * BLOCK_SIZE)

    def draw_sidebar(self, next_shape_id, score):
        self.screen.fill(
            COLOR_SIDEBAR_BORDER, (GRID_WIDTH, 0, SIDEBAR_BORDER, GAME_HEIGHT)
        )

        self.draw_shape(
            SHAPES[next_shape_id],
            next_shape_id,
            SIDEBAR_CONTEXT_X,
            SIDEBAR_CONTEXT_Y
        )

        score_surface = self.font.render("Score:", True, COLOR_FONT)
        self.screen.blit(score_surface, (SIDEBAR_CONTEXT_X, BLOCK_SIZE * 5))

        score_surface = self.font.render(f"{score: 06}", True, COLOR_FONT)
        self.screen.blit(score_surface, (SIDEBAR_CONTEXT_X, BLOCK_SIZE * 6))

    def draw_grid(self, grid):
        for i, row in enumerate(grid.matrix):
            for j, shape_id in enumerate(row):
                color = COLOR_EMPTY_BLOCK if shape_id == EMPTY_BLOCK else SHAPE_COLORS[shape_id]
                self.draw_block(color, j * BLOCK_SIZE, i * BLOCK_SIZE)

    def draw_game_over_overlay(self):
        overlay = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        overlay.set_alpha(ALPHA_GAME_OVER_OVERLAY)
        overlay.fill(COLOR_GAME_OVER_OVERLAY)
        self.screen.blit(overlay, (0, 0))

        text_surface = self.font.render("Game Over!", True, COLOR_FONT)
        text_center = text_surface.get_rect().centerx
        self.screen.blit(text_surface, (GRID_WIDTH // 2 - text_center, BLOCK_SIZE * 10))

    def render(self, state: GameState):
        self.screen.fill(COLOR_BACKGROUND)

        self.draw_grid(state.grid)

        self.draw_shape(
            state.piece.shape,
            state.piece.shape_id,
            state.piece.x * BLOCK_SIZE,
            state.piece.y * BLOCK_SIZE
        )

        self.draw_sidebar(state.next_shape_id, state.score)

        if state.is_game_over:
            self.draw_game_over_overlay()

        pygame.display.flip()