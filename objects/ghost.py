from typing import List

import pygame

from misc import get_ghost_path
from .character import CharacterObject


class GhostBase(CharacterObject):
    filenames: List[str] = [
        get_ghost_path('blue', 'up1.png'),
        get_ghost_path('blue', 'down1.png'),
        get_ghost_path('blue', 'left1.png'),
        get_ghost_path('blue', 'right1.png'),
        get_ghost_path('crazy_ghost', '1.png')
    ]
    filename: str = filenames[1]

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (14, 14))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (14, 14))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (14, 14))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (14, 14))
    scared_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[4]), (14, 14))

    def __init__(self, game, x, y) -> None:
        super().__init__(game, x, y)
        self.image = self.up_img_resized
        self.status = 'normal'

    def test_move(self) -> None:
        pass

    def process_logic(self) -> None:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        self.test_move()
        self.status = 'scared' if keys[pygame.K_x] else 'normal'
        if self.status == 'scared':
            self.image = self.scared_img_resized
