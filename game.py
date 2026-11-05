# game.py
import pygame as pg

import settings as st
from object import Object
from states import GameState


class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen: pg.Surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.object: Object = Object(50, 50)
        self.state: GameState = GameState.PLAYING

    def run(self) -> None:
        while self.state != GameState.QUIT:
            self.events()
            self.update()
            self.render()
            self.clock.tick(st.FPS)
        pg.quit()

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = GameState.QUIT
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.state = GameState.QUIT
                elif event.key == pg.K_p:
                    self.state = (GameState.PAUSED if self.state == GameState.PLAYING
                                  else GameState.PLAYING)

    def update(self) -> None:
        if self.state == GameState.PLAYING:
            self.object.update()

    def render(self) -> None:
        self.screen.fill(pg.Color("black"))
        pg.draw.rect(self.screen, self.object.color, self.object.body)
        pg.display.flip()
