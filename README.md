# Tetris

Tetris (classic game) made with JavaScript.

### Game Elements

1. Grid of Blocks (10 x 20)
2. Current Piece
3. Gravity (pulls the pieces down)
4. Sidebar
   - to show the next piece
   - show current score
5. Game Over Screen

### All Shapes (Tetrominos)

![alt text](assets/readme%20images/tetrominos.png)

### User Input

- Left - Move left
- Right - Move right
- Down - Move down
- Up - Rotate
- Space - Hard Drop
- R - Restart

### Game Loop

- Grid [2D array] - 20 rows x 10 columns
- Current Piece:
  - Position (x, y)
  - Shape [2D array]
  - Shape type (color)
- Score
- Gravity (progress and speed)
- is game over

![Game Layout](assets/readme%20images/layout.png)

### Piece Rotation

![Piece Rotation Pattern](assets/readme%20images/rotation-pattern.png)

Basically - `[i][j] -> [j][size - 1 - i]`

### Clearing Full Lines

![Clearing Logic](assets/readme%20images/clearing-logic.png)
