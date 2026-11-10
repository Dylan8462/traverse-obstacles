# object.py

from pathlib import Path

import pygame as pg

import settings as st
from states import Facing, Status


class Object:
    def __init__(self) -> None:
        self.sheet: pg.Surface = pg.image.load(Path(__file__).parent / "assets" / "SpriteSheet.png").convert_alpha()

        self.dir = Facing.NONE
        self.state = Status.LIVING

    def build_images(self, left: int, top: int, w: int = 15, h: int = 15) -> dict[Facing, pg.Surface]:
        images: dict[Facing, pg.Surface] = {}

        frame: pg.Rect = pg.Rect(left, top, w, h)

        for dir in Facing:
            if dir is Facing.NONE:
                continue

            raw = self.sheet.subsurface(frame)

            images[dir] = pg.transform.scale(raw, (frame.w * st.SCALE, frame.h * st.SCALE))

        images[Facing.RIGHT] = pg.transform.flip(images[Facing.RIGHT], True, False)
        images[Facing.UP] = pg.transform.rotate(images[Facing.LEFT], -90)
        images[Facing.DOWN] = pg.transform.flip(images[Facing.UP], False, True)
        
        return images
