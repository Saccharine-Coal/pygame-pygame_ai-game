import pygame as pg
import pygame_ai as pai

import settings


class GameObject(object):
    def __init__(self, rect:pg.Rect) -> None:
        self.rect = rect

    def update(self, dt: float):
        pass

    def draw(self, surface:pg.Surface):
        surface.blit(self.image, self.rect)


class Sprite2(pai.gameobject.GameObject):
    """Pygame ai is used to control sprites. Much of the code is adapted from https://pygame-ai.readthedocs.io/en/latest/guide.html"""
    def __init__(self, img_surf=..., pos=..., max_speed=30, max_accel=20, max_rotation=60, 
            max_angular_accel=50
        ):
        # Apply Drag to all Sprite 2
        self.drag = settings.DRAG
        super().__init__(img_surf=img_surf, pos=pos, max_speed=max_speed, 
            max_accel=max_accel, max_rotation=max_rotation, 
            max_angular_accel=max_angular_accel
        )

    def draw(self, surface:pg.Surface):
        surface.blit(self.image, self.rect)


class Player(Sprite2):
    def __init__(self, xy:tuple, size:tuple):
        # set player settings from the file settings
        image_surface = settings.PLAYER_IMG
        image_surface = pg.transform.scale(image_surface, size)
        max_speed, max_accel = settings.PLAYER_MAX_SPEED, settings.PLAYER_MAX_ACCEL
        max_rotation, max_angular_accel = settings.PLAYER_MAX_ROTATION, settings.PLAYER_MAX_ANGULAR_ACCEL
        # Create player steering
        self.steering = settings.PLAYER_STEERING() # initialize steering
        super().__init__(img_surf=image_surface, pos=xy, max_speed=max_speed, 
            max_accel=max_accel, max_rotation=max_rotation, 
            max_angular_accel=max_angular_accel    
        )

    def update(self, tick):
        self.steer(self.steering, tick)
        self.rect.move_ip(self.velocity)
        # Apply drag
        self.steer(self.drag.get_steering(self), tick)
        # Restart player steering
        self.steering.reset()

    def accelerate(self, dx:int=0, dy:int=0):
        # [0] x acceleration, [1] y acceleration
        self.steering.linear[0] += self.max_accel*dx
        self.steering.linear[1] += self.max_accel*dy

class EnemyNPC(Sprite2):
    
    def __init__(self, xy:tuple, size:tuple, player):
        # set enemy settings from the file settings
        image_surface = settings.ENEMY_IMG
        image_surface = pg.transform.scale(image_surface, size)
        max_speed, max_accel = settings.ENEMY_MAX_SPEED, settings.ENEMY_MAX_ACCEL
        max_rotation, max_angular_accel = settings.ENEMY_MAX_ROTATION, settings.ENEMY_MAX_ANGULAR_ACCEL
        super().__init__(img_surf=image_surface, pos=xy, max_speed=max_speed, 
            max_accel=max_accel, max_rotation=max_rotation, 
            max_angular_accel=max_angular_accel    
        )
        # Create a placeholder for the AI
        self.ai = settings.ENEMY_STEERING(self, player) # initialize ai
        
    def update(self, tick):
        steering = self.ai.get_steering()
        self.steer(steering, tick)
        self.rect.move_ip(self.velocity)
        # Apply drag
        self.steer(self.drag.get_steering(self), tick)

