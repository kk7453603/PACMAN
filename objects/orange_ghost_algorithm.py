import pygame
from .ghost import GhostBase
from .field import FieldOblect
from misc import get_ghost_path


def process_logic(self) -> None:
    self.define_direction()
    x1 = self.rect.x
    y1 = self.rect.y
    point_i = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[1]
    point_j = self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.pos_on_field[0]
    raw_distance = ((point_j - x1) ** 2 + (point_i - y1) ** 2) ** 0.5
    distance = raw_distance / cell_height
    if (distance > 8):
    #Red Ghost Behavior
        self.move(self.status, point i, point_j)
    else:
    #Left Down Corner
        self.move(self.status, 29.5 * cell_height, 1.5 * cell_width)
