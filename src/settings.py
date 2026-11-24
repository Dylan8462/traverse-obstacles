# settings.py

from pathlib import Path

FPS: int = 60

LAYOUT: str = "GRRGRRRGRRGRRRG"   # top -> bottom; (G)rass, (R)oad

TILE: int = 16

COLS: int = 13
ROWS: int = len(LAYOUT)

WIDTH: int = COLS * TILE
HEIGHT: int = ROWS * TILE

ASSETS_DIR: Path = Path(__file__).resolve().parent.parent / "assets"
SPRITESHEET: Path = ASSETS_DIR / "sprites.png"
