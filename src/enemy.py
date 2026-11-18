# enemy.py

import pygame as pg

import settings as st
from object import Object
from states import Facing


class Enemy(Object):
    def __init__(self) -> None:
        super().__init__()

        self.images = super().build_images(75, 30, 30, 15)
        self.dir: Facing = Facing.RIGHT
        self.body = self.images[self.dir].get_rect(center = (800, 300))
        self.image = self.images[self.dir]

        self.speed: float = 2.0

    def update(self, screen_rect: pg.Rect) -> None:
        self.body.move_ip(self.speed, 0)

        if not screen_rect.contains(self.body):
            self.speed *= -1

            if self.dir is Facing.LEFT:
                self.dir = Facing.RIGHT
            elif self.dir is Facing.RIGHT:
                self.dir = Facing.LEFT

        self.image = self.images[self.dir]
