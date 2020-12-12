import pygame
from typing import List
from .ghost import GhostBase
from misc import get_ghost_path


class PinkGhostObject(GhostBase):
    filenames: List[str] = [
        get_ghost_path('pink', 'up1.png'),
        get_ghost_path('pink', 'down1.png'),
        get_ghost_path('pink', 'left1.png'),
        get_ghost_path('pink', 'right1.png')
    ]

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (17, 17))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (17, 17))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (17, 17))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (17, 17))
