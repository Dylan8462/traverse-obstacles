# player.py

import pygame as pg
import settings as st
from object import Object
from states import Facing, Status

KEYS: dict[int, Facing] = {
    pg.K_UP: Facing.UP, pg.K_w: Facing.UP,
    pg.K_DOWN: Facing.DOWN, pg.K_s: Facing.DOWN,
    pg.K_LEFT: Facing.LEFT, pg.K_a: Facing.LEFT,
    pg.K_RIGHT: Facing.RIGHT, pg.K_d: Facing.RIGHT,
}

STEP: dict[Facing, tuple[int, int]] = {
    Facing.UP: (0, -1),
    Facing.DOWN: (0, 1),
    Facing.LEFT: (-1, 0),
    Facing.RIGHT: (1, 0),
}


class Player(Object):
    """
     Playable chicken representation
     Moves in all directions and collides with cars
    """
    def __init__(self) -> None:
        super().__init__(0, 0, Object.sprite(48, 16))

        self.images: dict[Facing, pg.Surface] = {
            Facing.UP: Object.sprite(48, 16, rotate = 90),
            Facing.DOWN: Object.sprite(48, 16, rotate = -90),
            Facing.LEFT: Object.sprite(48, 16, flip = True),
            Facing.RIGHT: Object.sprite(48, 16),
        }
        
        self.score: int = 0
        self.reset()

        self.x: int
        self.y: int

        self.col: int
        self.row: int

        self.dir: Facing
        self.state: Status

        self.image: pg.Surface
        

    # Reset chicken to bottom middle 
    def reset(self) -> None:
        self.col = st.COLS // 2
        self.row = st.ROWS - 1
        
        self.dir = Facing.UP
        self.state = Status.LIVING
        
        self.update()

    def hitbox(self) -> pg.Rect:
        return pg.Rect(round(self.x) + 3, round(self.y) + 3, 10, 10) # 10 x 10 instead of 16 x 16

    def update(self) -> None:
        self.x = self.col * st.TILE
        self.y = self.row * st.TILE
        
        self.image = self.images[self.dir]

        if self.state is Status.DEAD:
            self.reset()

    def die(self) -> None:
        self.state = Status.DEAD
        self.score = 0

    # Read key input from events in Game
    def keyvent(self, key: int) -> None:
        if key not in KEYS:
            return

        self.dir = KEYS[key]
        
        dx, dy = STEP[self.dir]
        
        self.col = max(0, min(st.COLS - 1, self.col + dx)) # clamp player inside bounds
        self.row = max(0, min(st.ROWS - 1, self.row + dy)) # same but bottom / top
