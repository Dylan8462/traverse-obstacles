# player.py

import pygame as pg

import settings as st
from object import Object
from states import Facing, Status


class Player(Object):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.images = super().build_images(105, 30)
        self.dir: Facing = Facing.RIGHT
        self.body = self.images[self.dir].get_rect(center = (x, y - 30))
        self.image = self.images[self.dir]
        
        self.move_tiles: float = 15 * st.SCALE
        
    def update(self) -> None:

        
        self.image = self.images[self.dir]

    def die(self) -> None:
        self.state = Status.DEAD

    def keyvent(self, key: int) -> None:
        match key:
            case pg.K_LEFT:
                self.body.move_ip(-self.move_tiles, 0)
                self.dir = Facing.LEFT
            case pg.K_RIGHT:
                self.body.move_ip(self.move_tiles, 0)
                self.dir = Facing.RIGHT
            case pg.K_UP:
                self.body.move_ip(0, -self.move_tiles)
                self.dir = Facing.UP
            case pg.K_DOWN:
                self.body.move_ip(0, self.move_tiles)
                self.dir = Facing.DOWN
