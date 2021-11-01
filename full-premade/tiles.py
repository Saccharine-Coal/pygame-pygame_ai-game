from random import randint

import pygame as pg

import sprites
import settings


class Tile(sprites.GameObject):
    def __init__(self, xy: tuple, size: tuple, image: pg.Surface) -> None:
        self.image = pg.transform.scale(image, size)
        rect = pg.Rect(xy, size)
        super().__init__(rect)


class TileA(Tile):
    def __init__(self, xy: tuple, size: tuple) -> None:
        image = settings.TILE_A_IMG
        # random tile orientation
        random_angle = randint(0, 3)*90
        rotated_image = pg.transform.rotate(image, random_angle)
        super().__init__(xy, size, rotated_image)


class TileB(Tile):
    def __init__(self, xy: tuple, size: tuple) -> None:
        image = settings.TILE_B_IMG
        super().__init__(xy, size, image)


class TileC(Tile):
    def __init__(self, xy: tuple, size: tuple) -> None:
        image = settings.TILE_C_IMG
        super().__init__(xy, size, image)