# player.py

import pygame as pg

import settings as st
from object import Object
from states import Facing


class Player(Object):
    def __init__(self, w: float, h: float) -> None:
        super().__init__(w, h)

        self.images = self.build_images()
        self.dir: Facing = Facing.UP
        self.body = self.images[self.dir].get_rect(center = (500, 500))
        
        self.move_tiles: float = 15 * st.SCALE
        
    def update(self) -> None:
        self.image = self.images[self.dir]

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

    def build_images(self) -> dict[Facing, pg.Surface]:
        images: dict[Facing, pg.Surface] = {}

        frame: pg.Rect = pg.Rect(105, 30, 15, 15)

        for dir in Facing:
            if dir is Facing.NONE:
                continue

            raw = self.sheet.subsurface(frame)

            images[dir] = pg.transform.scale(raw, (frame.w * st.SCALE, frame.h * st.SCALE))

        images[Facing.RIGHT] = pg.transform.flip(images[Facing.RIGHT], True, False)
        images[Facing.UP] = pg.transform.rotate(images[Facing.LEFT], -90)
        images[Facing.DOWN] = pg.transform.flip(images[Facing.UP], False, True)
        
        return images
