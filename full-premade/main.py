from math import floor

import pygame as pg

import scenes
import settings


class Game:
    """This class handles initialization of the pygame object, pygame events, game updates, and pygame drawing."""
    def __init__(self):
        self.new()

    # UNMUTABLE LOOP ---------------------------------------

    def new(self):
        """Initialize pygame characteristics, programs, and attributes here.
        Iniitialize starting scene here."""
        pg.init()
        flags = pg.DOUBLEBUF #| pg.FULLSCREEN | pg.HWSURFACE
        self.screen = pg.display.set_mode(settings.SCREEN_SIZE, flags)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        font = pg.font.Font('freesansbold.ttf', settings.FONT_SIZE)
        self.active_scene = scenes.GameScene(self.screen, font, (0, 0, 0))

    def run(self):
        """Runs pygame."""
        while True:
            # ACTUAL GAME LOOP
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.render()

    # MUTABLE LOOPS ------------------------------------

    def events(self):
        """Catch all pygame events here."""
        self.active_scene.handle_events()

    def update(self):
        """Update active scene here."""
        self.active_scene = self.active_scene.update(self.dt)
        
    def render(self):
        """Render directly to the pygame display here."""
        pg.display.set_caption(f"FPS: {floor(self.clock.get_fps())}")
        self.active_scene.render()
        pg.display.flip()


# Create game object.
g = Game()
g.run()


