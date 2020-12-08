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

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (35, 35))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (35, 35))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (35, 35))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (35, 35))
    scared_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[4]), (35, 35))

    def __init__(self, game) -> None:
        super().__init__(game)
        self.image = self.up_img_resized
        self.status = 'normal'
        self.obj_type = 'ghost'

    def test_move(self) -> None:
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.rect.y += self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.down_img_resized
        elif keys[pygame.K_UP]:
            self.rect.y -= self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.up_img_resized
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.left_img_resized
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.right_img_resized

    def get_type(self) -> str:
        return self.obj_type

    def process_logic(self) -> None:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        self.test_move()
        self.status = 'scared' if keys[pygame.K_x] else 'normal'
        if self.status == 'scared':
            self.image = self.scared_img_resized
