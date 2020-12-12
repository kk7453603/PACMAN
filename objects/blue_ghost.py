import pygame
from .ghost import GhostBase


class BlueGhostObject(GhostBase):
    def process_logic(self) -> None:
        self.define_direction()
        if self.status == 'normal':
            distanse_x = (self.game.scenes[self.game.MAIN_SCENE_INDEX].red_ghost.rect.x -
                          self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.rect.x) // 17
            distanse_y = (self.game.scenes[self.game.MAIN_SCENE_INDEX].red_ghost.rect.y -
                          self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.rect.y) // 17
            point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1] + distanse_y
            point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0] + distanse_x
            self.move_ghost(self.status, point_i, point_j)
        elif self.status == 'scared':
            self.move_ghost(self.status, 26, 2)
            self.scare_to_normal()
