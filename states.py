# states.py

from enum import Enum, auto


class GameState(Enum):
    START = auto()
    PLAYING = auto()
    PAUSED = auto()
    GAMEOVER = auto()
    QUIT = auto()
