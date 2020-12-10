import pygame
from typing import List
from .ghost import GhostBase
from misc import get_ghost_path


class RedGhostObject(GhostBase):
    filenames: List[str] = [
        get_ghost_path('red', 'up1.png'),
        get_ghost_path('red', 'down1.png'),
        get_ghost_path('red', 'left1.png'),
        get_ghost_path('red', 'right1.png')
    ]

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (14, 14))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (14, 14))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (14, 14))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (14, 14))
