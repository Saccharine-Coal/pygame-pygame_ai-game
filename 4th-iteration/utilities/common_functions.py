import os

import pygame as pg

def load_image(directory:str, name:str) -> pg.Surface:
    try:
        return pg.image.load(os.path.join(directory, name))
    except:
        raise FileNotFoundError(f"{name} is not in {directory}")

def join_paths(directory:str, subdirs:list):
    return os.path.join(directory, *subdirs)