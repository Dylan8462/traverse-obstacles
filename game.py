# game.py

import os
import warnings
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
warnings.filterwarnings("ignore", category=RuntimeWarning, module="importlib._bootstrap")
import pygame

pygame.display.init()
screen = pygame.display.set_mode((0, 0))
clock = pygame.time.Clock()
running = True
square = pygame.Rect(0, 0, 50, 50)

while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                square.move(0, -10)
            if event.key == pygame.K_DOWN :
                square.move(0, 10)
            if event.key == pygame.K_RIGHT :
                square.move(10, 0)
            if event.key == pygame.K_LEFT :
                square.move(-10, 0)
    
    screen.fill("black")
    
    pygame.draw.rect(screen, "white", square)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
