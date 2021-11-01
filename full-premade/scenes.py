import sys

import pygame as pg
from pygame import font

import worlds
import utilities.pg_text
import settings


class Scene:
    def __init__(self, screen: pg.Surface, font: font.Font, background_color: tuple) -> None:
        self.screen, self.font, self.background_color = screen, font, background_color
        self.surface = pg.Surface(screen.get_rect().size)
        self.rect = pg.Rect((0, 0), self.surface.get_rect().size)
        self.next = self

    @staticmethod
    def exit():
        """Terminate pygame and exit the program."""
        pg.quit()
        sys.exit()

    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.exit()
        return events

    def update(self, dt:float):
        return self.next

    def render(self):
        self.surface.fill(self.background_color)


class GameScene(Scene):
    def __init__(self, screen: pg.Surface, font: font.Font, background_color: tuple):
        super().__init__(screen, font, background_color)
        self.world = worlds.World2((0, 0), settings.FOG_OF_WAR)

    def handle_events(self):
        events = super().handle_events()
        self.world.check_events(events)
        return events

    def update(self, dt: float) -> Scene:
        self.world.update(dt)
        if self.world.goal_complete:
            self.next = WinScene(self.screen, self.font, self.background_color)
        if self.world.enemy_collision:
            self.next = FailScene(self.screen, self.font, self.background_color)
        return super().update(dt)
    
    def render(self):
        super().render()
        self.world.render(self.surface)
        self.screen.blit(self.surface, self.rect.topleft)


class WinScene(Scene):
    def __init__(self, screen: pg.Surface, font: font.Font, background_color: tuple) -> None:
        super().__init__(screen, font, background_color)
        self.message_sur = utilities.pg_text.get_text(self.font, settings.WIN_MESSAGE, (0, 255, 0))

    def render(self):
        super().render()
        utilities.pg_text.blit_text(self.surface, self.message_sur, self.rect.center, 0, True, 0, True)
        self.screen.blit(self.surface, self.rect.topleft)

class FailScene(Scene):
    def __init__(self, screen: pg.Surface, font: font.Font, background_color: tuple) -> None:
        super().__init__(screen, font, background_color)
        self.message_sur = utilities.pg_text.get_text(self.font, settings.LOSS_MESSAGE, (255, 0, 0))

    def render(self):
        super().render()
        utilities.pg_text.blit_text(self.surface, self.message_sur, self.rect.center, 0, True, 0, True)
        self.screen.blit(self.surface, self.rect.topleft)
