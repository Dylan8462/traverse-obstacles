# game.py
import pygame as pg

import settings as st
from object import Object
from player import Player
from states import GameState


class Game:
    def __init__(self) -> None:
        pg.init()
        
        self.screen: pg.Surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.clock: pg.time.Clock = pg.time.Clock()
        
        self.state: GameState = GameState.PLAYING
        
        self.player: Player = Player(30, 30)
        
    # main game loop 
    def run(self) -> None:
        while self.state != GameState.QUIT:
            self.events()
            self.update()
            self.render()
            
            self.clock.tick(st.FPS)
            
        pg.quit()

    # all events, game, key, etc
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
                else:
                    self.player.keyvent(event.key)

    # all object update methods
    def update(self) -> None:
        if self.state == GameState.PLAYING:
            self.player.update()

        print(self.player.sheet.get_size())

    # render all items
    def render(self) -> None:
        self.screen.fill(pg.Color("black"))
        self.screen.blit(self.player.image, self.player.body)
        pg.display.flip()
