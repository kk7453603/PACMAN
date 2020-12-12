import pygame
from typing import List
from .ghost import GhostBase
from misc import get_ghost_path


class OrangeGhostObject(GhostBase):
    filenames: List[str] = [
        get_ghost_path('orange', 'up1.png'),
        get_ghost_path('orange', 'down1.png'),
        get_ghost_path('orange', 'left1.png'),
        get_ghost_path('orange', 'right1.png')
    ]

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (17, 17))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (17, 17))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (17, 17))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (17, 17))

    def process_logic(self) -> None:
        self.define_direction()
        x1 = self.rect.x
        y1 = self.rect.y
        point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1]
        point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0]
        raw_distance = ((point_j - x1) ** 2 + (point_i - y1) ** 2) ** 0.5
        distance = raw_distance / 17
        if self.status == 'normal':
            if distance > 8:
                # Red Ghost Behavior
                self.move(self.status, point_i, point_j)
            else:
                # Left Down Corner
                self.move(self.status, 29.5 * 17, 1.5 * 17)
        elif self.status == 'scared':
            self.move(self.status, 29, 26)
            self.scare_to_normal()
