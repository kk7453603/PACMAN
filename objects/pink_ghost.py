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

    def process_logic(self) -> None:
        self.define_direction()
        if self.status == 'normal':
            pacman_direction = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.direction
            point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1]
            point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0]
            if pacman_direction == 'UP':
                point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1] - 4
                point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0]
                if point_i < 0:
                    point_i = 0
            elif pacman_direction == 'DOWN':
                point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1] + 4
                point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0]
                if point_i > 30:
                    point_i = 30
            elif pacman_direction == 'LEFT':
                point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1]
                point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0] - 4
                if point_j < 0:
                    point_j = 0
            elif pacman_direction == 'RIGHT':
                point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1]
                point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0] + 4
                if point_j > 27:
                    point_j = 27
            self.move(self.status, point_i, point_j)
        elif self.status == 'scared':
            self.move(self.status, 4, 26)
            self.scare_to_normal()
