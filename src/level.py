# level.py

import random

import pygame as pg
import settings as st
from enemy import Enemy
from object import Object


class Level:
    """
     Pre-rendered grass/road background
     plus the cars on it
    """

    def __init__(self) -> None:
        # background is drawn once here instead of tile by tile every frame
        self.background: pg.Surface = pg.Surface((st.WIDTH, st.HEIGHT))
        self.cars: list[Enemy] = []
        
        grass = Object.sprite(0, 0)
        road = Object.sprite(32, 0)
        
        for row, kind in enumerate(st.LAYOUT):
            tile = road if kind == "R" else grass
            
            for col in range(st.COLS):
                self.background.blit(tile, (col * st.TILE, row * st.TILE))

        self.populate()

    # Put cars on every row
    def populate(self) -> None:
        self.cars.clear()
        
        for row, kind in enumerate(st.LAYOUT):
            if kind != "R":
                continue
            
            direction = random.choice((-1, 1))
            speed = random.uniform(30, 70)
            
            for i in range(3):
                self.cars.append(Enemy(row, i * 80 + random.randint(0, 30), direction, speed))

    def update(self, dt: float) -> None:
        for car in self.cars:
            car.update(dt)

    def draw(self, canvas: pg.Surface) -> None:
        canvas.blit(self.background, (0, 0))
        for car in self.cars:
            car.draw(canvas)
