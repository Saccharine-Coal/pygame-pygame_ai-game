import pygame as pg
from pygame import font


def get_text_surfaces(pg_font: font.Font, string_list: list, font_color: tuple=(0, 0, 0), 
    background_color: tuple=None) -> tuple:
    return tuple(get_text(pg_font, string, font_color, background_color) for string 
        in string_list)

def get_text(pg_font: font.Font, string: str, font_color: tuple=(0, 0, 0), 
    background_color: tuple=None) -> pg.Surface:
    if background_color is not None:
        text_surface = pg_font.render(string, True, font_color, background_color)
    else:
            text_surface = pg_font.render(string, True, font_color)
    return text_surface

def blit_text(target_surface: pg.Surface, surface_to_blit: pg.Surface, xy: tuple, i :int=0,
    descending: bool=True, line_spacing: int=0, centered:bool=False):

    def center_surface_about_point(surface: pg.Surface, xy: tuple) -> tuple:
        w, h = surface.get_rect().size[:]
        x, y = xy[:]
        return (x - round(w/2), y + round(h/2))

    x, y = xy[:]
    w, h = surface_to_blit.get_rect().size[:]
    if descending:
        xy = x, y + i*(h + line_spacing)
    else:
        xy = x, y - i*(h + line_spacing)
    if centered:
        xy = center_surface_about_point(surface_to_blit, xy)
    target_surface.blit(surface_to_blit, xy)

def blit_text_surfaces(target_surface: pg.Surface, text_surfaces: list, xy: tuple, 
    descending: bool=True, line_spacing: int=0, centered: bool=False):
    for i, surface in enumerate(text_surfaces):
        blit_text(target_surface, surface, xy, i, descending, line_spacing, centered)