import csv
import os
from random import randint

import pygame as pg

import sprites
import tiles
import settings


TILESIZE = settings.TILESIZE
FOVSIZE = settings.FOVSIZE

class World2(object):
    def __init__(self, ORIGIN:tuple, fov) -> None:
        self.ORIGIN, self.fov = ORIGIN , fov
        self.fov_size, self.TILESIZE = FOVSIZE, TILESIZE
        # grid
        self.array = self.csv_to_array(settings.ASSETS_DIR, "map.csv")
        self.size = (max(map(len, self.array)), len(self.array))
        # tileA are floor, tileB are walls, tileC are goals
        self.floors = self.get_tiles(self.array, 1, tiles.TileA)
        self.walls = self.get_tiles(self.array, 0, tiles.TileB)
        self.goals = self.get_tiles(self.array, 2, tiles.TileC)
        self.grid = self.walls + self.floors + self.goals
        # surface
        self.surface = pg.Surface((TILESIZE*self.size[0], TILESIZE*self.size[1]), pg.SRCALPHA)
        UNIT_SIZE = (round(TILESIZE/2), round(TILESIZE/2))
        # boundary rect
        self.rect = pg.Rect(ORIGIN, tuple(TILESIZE*element for element in self.size))
        # player
        self.player = sprites.Player((TILESIZE/2, TILESIZE/2), UNIT_SIZE)
        # NPCs
        self.enemies = tuple(sprites.EnemyNPC((randint(settings.TOTAL_SIZE[0]/2, settings.TOTAL_SIZE[0]), 
            randint(0, settings.TOTAL_SIZE[1])), UNIT_SIZE, self.player) 
            for i in range(0, settings.NUMBER_OF_ENEMIES, 1)
        )
        self.enemy_collision, self.goal_complete = False, False
    ## INIT ------------------------------------------------------------------------------
    def get_tiles(self, array:tuple, FLAG:int, TILE:tiles.Tile) -> tuple:
        X_OFFSET, Y_OFFSET = self.ORIGIN[:]
        tiles = []
        for row_number, row in enumerate(array):
            for col_number, value in enumerate(row):
                if value == FLAG:
                    topleft = ((col_number*self.TILESIZE)+X_OFFSET, 
                            (row_number*self.TILESIZE)+Y_OFFSET)
                    size = (self.TILESIZE, self.TILESIZE)
                    tiles.append(TILE(topleft, size))
        return tuple(tiles)

    @staticmethod
    def csv_to_array(dir: str, name: str) -> tuple:
        path = os.path.join(dir, name)
        rows = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file)
            for i, line in enumerate(csv_reader):
                if i == 0:
                    # headers
                    continue
                else:
                    rows.append(tuple(int(element) for element in line))
        return tuple(rows)

    # EVENTS ------------------------------------------------------------------------------
    
    def check_events(self, events):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.player.accelerate(dy=-1)
        if keys[pg.K_DOWN]:
            self.player.accelerate(dy=1)
        if keys[pg.K_LEFT]:
            self.player.accelerate(dx=-1)
        if keys[pg.K_RIGHT]:
            self.player.accelerate(dx=1)

    # UPDATE -------------------------------------------------------------------------------

    def update(self, dt:float) -> bool:
        self.player.update(dt)
        self.check_player_collision()
        if self.check_npc_collision():
            self.enemy_collision = True
        self.goal_complete = self.check_goal_collision()
        for npc in self.enemies:
            npc.update(dt)

    def check_player_collision(self):
        """Check if the player can be translated. If the player cannot be translated, 
        then the player's velocity is set to 0."""
        new_rect = self.player.rect.move(self.player.velocity)
        # TODO pixel perfect collision
        if not (self._is_wall_colliding(new_rect) is False
            and self._is_in_grid(new_rect) is True):
            # rect collision
            BOUNCE = settings.PLAYER_BOUNCE
            vx, vy = self.player.velocity[:]
            self.player.velocity.update((-vx*BOUNCE, -vy*BOUNCE))

    def check_npc_collision(self) -> bool:
        for npc in self.enemies:
            if npc.rect.colliderect(self.player.rect) == 1:
                # npc and player rect overlap
                # TODO pixel perfect collision
                if self.player.rect.collidepoint(npc.rect.center) == 1:
                    # npc center is in player rect
                    return True
        return False

    def _is_wall_colliding(self, target_rect:pg.Rect) -> bool:
        """Check if target rect collides with any rects in grid."""
        for tile in self.walls:
            if target_rect.colliderect(tile.rect):
                # rect-rect collision
                if tile.rect.collidepoint(target_rect.center):
                    # rect-point collision
                    return True
        return False

    def _is_in_grid(self, target_rect:pg.Rect) -> bool:
        """Check if center of rect is in boundary rect."""
        if self.rect.collidepoint(target_rect.center) == 1:
            # in rect
            return True
        else:
            # not in rect
            return False

    def check_goal_collision(self) -> bool:
        """Check if center is a goal rect"""
        for tile in self.goals:
            if tile.rect.collidepoint(self.player.rect.center) is 1:
                return True
        return False

    # RENDER -------------------------------------------------------------------------------

    def render(self, surface:pg.Surface):
        self.surface.fill((0, 0, 0, 255))
        for tile in self.grid:
            tile.draw(surface)
        self.player.draw(surface)
        for npc in self.enemies:
            npc.draw(surface)
        if self.fov is True:
            self._draw_fov()
            surface.blit(self.surface, self.ORIGIN, special_flags=pg.BLEND_RGBA_MULT)

    def _draw_fov(self):
        x, y = self.player.rect.center
        dx, dy = self.ORIGIN[:]
        pg.draw.circle(self.surface, (100, 100, 100, 100), (x-dx, y-dy), self.fov_size)
