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

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (17, 17))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (17, 17))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (17, 17))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (17, 17))

    def process_logic(self) -> None:
        self.define_direction()
        if self.status == 'normal':
            point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1]
            point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0]
            self.move_ghost(self.status, point_i, point_j)
        elif self.status == 'scared':
            self.move_ghost(self.status, 5, 3)
            self.scare_to_normal()
