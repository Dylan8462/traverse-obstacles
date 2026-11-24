# game.py

import pygame as pg
import settings as st
from level import Level
from player import Player
from states import GameState


class Game:
    def __init__(self) -> None:
        pg.init()

        self.screen: pg.Surface = pg.display.set_mode((st.WIDTH, st.HEIGHT), pg.SCALED)
        self.clock: pg.time.Clock = pg.time.Clock()

        self.dt: float = 0.0
        self.state: GameState = GameState.PLAYING

        self.level: Level = Level()
        self.player: Player = Player()

        pg.display.set_caption("Traverse Obstacles")

    # main game loop
    def run(self) -> None:
        while self.state != GameState.QUIT:
            self.events()
            self.update()
            self.render()

            self.dt = min(self.clock.tick(st.FPS) / 1000, 0.05)   # seconds, capped

        pg.quit()

    # all events, game, key, etc
    def events(self) -> None:
        for event in pg.event.get():            # all events
            if event.type == pg.QUIT:               # leaving game
                self.state = GameState.QUIT
                
            elif event.type == pg.KEYDOWN:          # key events
                if event.key == pg.K_ESCAPE:            # also leaving game
                    self.state = GameState.QUIT
                    
                elif event.key == pg.K_p:               # pausing
                    self.state = (GameState.PAUSED
                                  if self.state == GameState.PLAYING
                                  else GameState.PLAYING)
                    
                elif self.state == GameState.PLAYING:   # player movement
                    self.player.keyvent(event.key)

    # all updates
    def update(self) -> None:
        if self.state != GameState.PLAYING:
            return

        # updates
        self.level.update(self.dt)
        self.player.update()

        # collisions
        for car in self.level.cars:
            if car.hitbox().colliderect(self.player.hitbox()):
                self.player.die()
                
        if self.player.row == 0:           # made it across
            self.player.score += 1
            self.level.populate()
            self.player.reset()

    # render all items
    def render(self) -> None:
        self.level.draw(self.screen)
        self.player.draw(self.screen)

        pg.display.set_caption(f"Traverse Obstacles - score {self.player.score}")
        pg.display.flip()
