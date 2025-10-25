// BLOCKS
const SHAPES = [
  // I
  [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
  ],
  // J
  [
    [1, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
  ],
  // L
  [
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
  ],
  // O
  [
    [0, 0],
    [0, 0],
  ],
  // S
  [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0],
  ],
  // T
  [
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 0],
  ],
  // Z
  [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 0],
  ],
];

// GAME CONSTANTS

const SHAPE_COLORS = [
  "#00BCD4",
  "#485FE5",
  "#FF9800",
  "#FFEB3B",
  "#4CAF50",
  "#A629BC",
  "#F44336",
];

const COLOR_SIDEBAR_BORDER = "#DDD";
const COLOR_EMPTY_BLOCK = "#343434";
const COLOR_GAME_OVERLAY = "#000000BB";
const COLOR_FONT = "#FFF";

const BLOCK_SIZE = 26;
const BLOCK_BACKGROUND = "#292929";

const GRAVITY_SPEED = 1;
const GRAVITY_ACCELERATION = 0.00001;
const GRAVITY_THRESHOLD = 1000; // after reaching this progress, the piece moves down

const GRID_COLS = 10;
const GRID_ROWS = 20;

const SIDEBAR_BORDER = 20;
const SIDEBAR_WIDTH_BLOCKS = 6;

const KEY_TO_INPUT_TYPE = {
  ArrowLeft: "moveLeft",
  ArrowRight: "moveRight",
  ArrowDown: "moveDown",
  ArrowUp: "rotate",
  " ": "hardDrop",
  r: "restart",
};

// COMPUTED CONSTANTS

const GRID_WIDTH = GRID_COLS * BLOCK_SIZE;
const GRID_HEIGHT = GRID_ROWS * BLOCK_SIZE;

const SIDEBAR_WIDTH = SIDEBAR_WIDTH_BLOCKS * BLOCK_SIZE;
const SIDEBAR_CONTENT_X = GRID_WIDTH + SIDEBAR_BORDER + BLOCK_SIZE;
const SIDEBAR_CONTENT_Y = BLOCK_SIZE;

const CANVAS_WIDTH = GRID_WIDTH + SIDEBAR_BORDER + SIDEBAR_WIDTH;
const CANVAS_HEIGHT = GRID_HEIGHT;

const BLOCK_EMPTY = -1;

function initCanvas() {
  const canvas = document.getElementById("game");
  canvas.width = CANVAS_WIDTH;
  canvas.height = CANVAS_HEIGHT;
  canvas.style.visibility = "visible";

  return canvas.getContext("2d");
}

function makeEmptyGrid() {
  return Array.from({ length: GRID_ROWS }, () => {
    return Array(GRID_COLS).fill(BLOCK_EMPTY);
  });
}

// returns a random value from [0 to n - 1]
function getRandomIndex(n) {
  return Math.floor(Math.random() * n);
}

function getRandomShapeId() {
  return getRandomIndex(SHAPES.length);
}

function createCurrentPiece(shapeId) {
  const shape = SHAPES[shapeId];

  return {
    shapeId,
    shape: [],
    position: {
      x: getRandomIndex(GRID_COLS - shape[0].length + 1),
      y: 0,
    },
  };
}

function getInitialState() {
  const initialShapeId = getRandomShapeId();

  return {
    isGameOver: false,
    score: 0,
    gravity: {
      progress: 0,
      speed: GRAVITY_SPEED,
    },
    currentPiece: createCurrentPiece(initialShapeId),
    nextShapeId: getRandomShapeId,
    grid: makeEmptyGrid(),
  };
}

function main() {
  const ctx = initCanvas();
  const state = getInitialState();

  console.log(state);
}

main();
