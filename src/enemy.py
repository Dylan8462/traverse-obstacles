# enemy.py

import random

import pygame as pg

import settings as st
from object import Object
from states import Facing

CAR_SPRITES = [(0, 32), (32, 32), (64, 32), (96, 32)]   # (left, top) on the sheet, 32 x 16 each


class Enemy(Object):
    """
     Representation of a car per row with road tiles
    """

    def __init__(self, row: int, x: float, direction: int, speed: float) -> None:
        left, top = random.choice(CAR_SPRITES)
        
        super().__init__(x, row * st.TILE, Object.sprite(left, top, 32, 16, flip = direction < 0))

        self.dir: Facing = Facing.RIGHT if direction > 0 else Facing.LEFT
        self.speed: float = direction * speed

        self.x: float

    def hitbox(self) -> pg.Rect:
        return self.rect().inflate(-4, -6)   # a bit smaller than the sprite
    
    def update(self, dt: float) -> None:
        self.x += self.speed * dt

        w: int = self.image.get_width()
        
        if self.speed > 0 and self.x > st.WIDTH + w: # right moving case -> wrap to left side
            self.x = -w
        elif self.speed < 0 and self.x < -w:         # left moving case -> wrap to right side 
            self.x = st.WIDTH + w
