import pygame as pg
import pygame_ai as pai

import utilities.common_functions


# world settings
TILE_DIMENSIONS = 7
TILESIZE = 128
FOVSIZE = TILESIZE*1.5
TOTAL_SIZE = (TILESIZE*TILE_DIMENSIONS, TILESIZE*TILE_DIMENSIONS)
FOG_OF_WAR = True

# screen settings
SCREEN_SIZE = TOTAL_SIZE
FPS = 60
FONT_SIZE = 40

# splash screens
WIN_MESSAGE = "You Win!"
LOSS_MESSAGE = "You Lost!"

# assets
ASSETS_DIR = "assets"

# verbose assets
VERBOSE_ASSETS_DIR = utilities.common_functions.join_paths(ASSETS_DIR, ["verbose-assets"])
VERBOSE_TILE_A_IMG = utilities.common_functions.load_image(VERBOSE_ASSETS_DIR, "tile_a.png")
VERBOSE_TILE_B_IMG = utilities.common_functions.load_image(VERBOSE_ASSETS_DIR, "tile_b.png")
VERBOSE_TILE_C_IMG = utilities.common_functions.load_image(VERBOSE_ASSETS_DIR, "tile_c.png")
VERBOSE_PLAYER_IMG = utilities.common_functions.load_image(VERBOSE_ASSETS_DIR, "player.png")
VERBOSE_ENEMY_IMG = utilities.common_functions.load_image(VERBOSE_ASSETS_DIR, "enemy.png")

# premade assets
PREMADE_ASSETS_DIR = utilities.common_functions.join_paths(ASSETS_DIR, ["premade-assets"])
PREMADE_TILE_A_IMG = utilities.common_functions.load_image(PREMADE_ASSETS_DIR, "premade-tile_a.png")
PREMADE_TILE_B_IMG  = utilities.common_functions.load_image(PREMADE_ASSETS_DIR, "premade-tile_b.png")
PREMADE_TILE_C_IMG  = utilities.common_functions.load_image(PREMADE_ASSETS_DIR, "premade-tile_c.png")
PREMADE_PLAYER_IMG  = utilities.common_functions.load_image(PREMADE_ASSETS_DIR, "premade-player.png")
PREMADE_ENEMY_IMG  = utilities.common_functions.load_image(PREMADE_ASSETS_DIR, "premade-enemy.png")

# class made assets
CLASS_ASSETS_DIR = utilities.common_functions.join_paths(ASSETS_DIR, ["class-assets"])
CLASS_TILE_A_IMG = utilities.common_functions.load_image(CLASS_ASSETS_DIR, "tile_a.png")
CLASS_TILE_B_IMG = utilities.common_functions.load_image(CLASS_ASSETS_DIR, "tile_b.png")
CLASS_TILE_C_IMG = utilities.common_functions.load_image(CLASS_ASSETS_DIR, "tile_c.png")
CLASS_PLAYER_IMG = utilities.common_functions.load_image(CLASS_ASSETS_DIR, "player.png")
CLASS_ENEMY_IMG = utilities.common_functions.load_image(CLASS_ASSETS_DIR, "enemy.png")

# active assets

# active is class made
TILE_A_IMG = CLASS_TILE_A_IMG
TILE_B_IMG = CLASS_TILE_B_IMG
TILE_C_IMG = CLASS_TILE_C_IMG
PLAYER_IMG = CLASS_PLAYER_IMG
ENEMY_IMG = CLASS_ENEMY_IMG

# active is premade
# TILE_A_IMG = PREMADE_TILE_A_IMG
# TILE_B_IMG = PREMADE_TILE_B_IMG
# TILE_C_IMG = PREMADE_TILE_C_IMG
# PLAYER_IMG = PREMADE_PLAYER_IMG
# ENEMY_IMG = PREMADE_ENEMY_IMG

# active is verbose
# TILE_A_IMG = VERBOSE_TILE_A_IMG
# TILE_B_IMG = VERBOSE_TILE_B_IMG
# TILE_C_IMG = VERBOSE_TILE_C_IMG
# PLAYER_IMG = VERBOSE_PLAYER_IMG
# ENEMY_IMG = VERBOSE_ENEMY_IMG

# Drag
DRAG = pai.steering.kinematic.Drag(15)

# Player Settings
PLAYER_MAX_SPEED = 15
PLAYER_MAX_ACCEL = 30
PLAYER_MAX_ROTATION = 40
PLAYER_MAX_ANGULAR_ACCEL = 30
PLAYER_STEERING = pai.steering.kinematic.SteeringOutput
PLAYER_BOUNCE = 0.3

# ENEMY Settings
NUMBER_OF_ENEMIES = 0
ENEMY_MAX_SPEED = 5
ENEMY_MAX_ACCEL = 20
ENEMY_MAX_ROTATION = 20
ENEMY_MAX_ANGULAR_ACCEL = 15
ENEMY_STEERING = pai.steering.kinematic.Seek

