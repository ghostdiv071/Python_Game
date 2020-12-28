from enum import Enum


class GameState(Enum):
    PLAYING = 0
    WIN = 1


class CellState(Enum):
    EMPTY = 0
    ACTIVE = 1
    MARKED = 2


class CellColor(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2


class CellShape(Enum):
    SQUARE = 0
    CIRCLE = 1


class Cell:
    def __init__(self, state: CellState, color: CellColor, shape: CellShape):
        self._state = state
        self._color = color
        self._shape = shape

    @property
    def state(self):
        return self._state

    @property
    def color(self):
        return self._color

    @property
    def shape(self):
        return self._shape


easy_level = {
    (0, 0): Cell(CellState(1), CellColor(0), CellShape(1)),  # 0 0
    (0, 1): Cell(CellState(0), CellColor(1), CellShape(0)),  # 0 1
    (0, 2): Cell(CellState(0), CellColor(0), CellShape(0)),  # 0 2
    (1, 0): Cell(CellState(0), CellColor(1), CellShape(1)),  # 1 0
    (1, 1): Cell(CellState(0), CellColor(0), CellShape(0)),  # 1 1
    (1, 2): Cell(CellState(0), CellColor(1), CellShape(1)),  # 1 2
    (2, 0): Cell(CellState(0), CellColor(1), CellShape(0)),  # 2 0
    (2, 1): Cell(CellState(0), CellColor(1), CellShape(1)),  # 2 1
    (2, 2): Cell(CellState(0), CellColor(0), CellShape(1)),  # 2 2
}


hard_level = {
    (0, 0): Cell(CellState(1), CellColor(0), CellShape(1)),  # 0 0
    (0, 1): Cell(CellState(0), CellColor(2), CellShape(1)),  # 0 1
    (0, 2): Cell(CellState(0), CellColor(1), CellShape(0)),  # 0 2
    (0, 3): Cell(CellState(0), CellColor(2), CellShape(0)),  # 0 3
    (1, 0): Cell(CellState(0), CellColor(1), CellShape(1)),  # 1 0
    (1, 1): Cell(CellState(0), CellColor(0), CellShape(0)),  # 1 1
    (1, 2): Cell(CellState(0), CellColor(0), CellShape(1)),  # 1 2
    (1, 3): Cell(CellState(0), CellColor(2), CellShape(0)),  # 1 3
    (2, 0): Cell(CellState(0), CellColor(0), CellShape(0)),  # 2 0
    (2, 1): Cell(CellState(0), CellColor(2), CellShape(1)),  # 2 1
    (2, 2): Cell(CellState(0), CellColor(2), CellShape(1)),  # 2 2
    (2, 3): Cell(CellState(0), CellColor(1), CellShape(0)),  # 2 3
    (3, 0): Cell(CellState(0), CellColor(0), CellShape(1)),  # 3 0
    (3, 1): Cell(CellState(0), CellColor(1), CellShape(0)),  # 3 3
    (3, 2): Cell(CellState(0), CellColor(2), CellShape(0)),  # 3 2
    (3, 3): Cell(CellState(0), CellColor(0), CellShape(1)),  # 3 3
}


class Game:
    def __init__(self, size: int):
        self._state = GameState.PLAYING
        self._size = size
        self._field = {}
        self.new_game()
        self._active = self._field.get((0, 0))

    @property
    def size(self):
        return self._size

    @property
    def state(self):
        return self._state

    @property
    def active(self):
        return self._active

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value: dict):
        self._field = value

    def new_game(self):
        if self.size == 3:
            self._field = easy_level
        elif self.size == 4:
            self._field = hard_level
        self._field.get((0, 0))._state = CellState.ACTIVE
        self._active = self._field.get((0, 0))
        for i in range(self.size):
            for j in range(self.size):
                if i != 0 or j != 0:
                    self._field.get((i, j))._state = CellState.EMPTY

        self._state = GameState.PLAYING

    def update_game_state(self):
        for i in range(self.size):
            for j in range(self.size):
                if self._field.get((i, j)).state == CellState.EMPTY:
                    self._state = GameState.PLAYING
                    return
        self._state = GameState.WIN
        if self._state == GameState.WIN:
            self.new_game()

    def left_mouse_click(self, row: int, col: int):
        if self.state == GameState.WIN:
            return
        cell = self._field.get((row, col))
        if cell.state in (CellState.MARKED, CellState.ACTIVE):
            return
        if cell.shape != self._active.shape and cell.color != self._active.color:
            return
        prev_row = list(self._field.keys())[list(self._field.values()).index(self._active)][0]
        prev_col = list(self._field.keys())[list(self._field.values()).index(self._active)][1]
        if row != prev_row and col != prev_col:
            return
        self._active._state = CellState.MARKED
        self._active = cell
        cell._state = CellState.ACTIVE
        self.update_game_state()
