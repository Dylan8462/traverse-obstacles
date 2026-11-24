# object.py

import pygame as pg
import settings as st
from states import Facing, Status


class Object:
    """
     Base for everything on screen
     Holds general variables and methods for player / enemy
    """

    _sheet: pg.Surface | None = None   # shared by every object, loaded once

    def __init__(self, x: float, y: float, image: pg.Surface) -> None:
        self.x: float = x
        self.y: float = y
        
        self.image: pg.Surface = image

        self.dir: Facing = Facing.NONE
        self.state: Status = Status.LIVING

    @classmethod
    # create sprite image
    def sprite(cls, left: int, top: int, w: int = 16, h: int = 16,
               flip: bool = False, rotate: int = 0) -> pg.Surface:
        if Object._sheet is None:
            Object._sheet = pg.image.load(str(st.SPRITESHEET)).convert_alpha()

        img = Object._sheet.subsurface(pg.Rect(left, top, w, h))
        
        if flip:
            img = pg.transform.flip(img, True, False)
        if rotate:
            img = pg.transform.rotate(img, rotate)
        return img

    # rect of object
    def rect(self) -> pg.Rect:
        return pg.Rect(round(self.x), round(self.y), self.image.get_size()[0], self.image.get_size()[1])

    def draw(self, canvas: pg.Surface) -> None:
        canvas.blit(self.image, (round(self.x), round(self.y)))
