# object.py

import pygame as pg


class Object:
    def __init__(self, w: float, h: float, c: pg.Color | None = None) -> None:
        self.body:  pg.Rect  = pg.Rect(0, 0, w, h)
        self.color: pg.Color = c if c is not None else pg.Color("white")
        self.speed: float = 3

    def update(self) -> None:
        keys = pg.key.get_pressed()

        dx = keys[pg.K_RIGHT] - keys[pg.K_LEFT]
        dy = keys[pg.K_DOWN] - keys[pg.K_UP]

        self.body.move_ip(dx * self.speed, dy * self.speed)
        
