# object.py

from pathlib import Path

import pygame as pg

from states import Facing


class Object:
    def __init__(self, width: float, height: float) -> None:
        self.sheet: pg.Surface = pg.image.load(Path(__file__).parent / "assets" / "SpriteSheet.png").convert_alpha()

        self.dir = Facing.NONE
