import pygame

from .character import CharacterObject
from .ghost import GhostBase


class Blue_ghost(GhostBase):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def check_points(self, pacman, blinky, mapp):
        # 2 точки после пакмана
        if mapp[pacman.x + 2][pacman.y] != 0:
            new_x = pacman.x + 2
            new_y = pacman.y
        elif mapp[pacman.x][pacman.y + 2] != 0:
            new_x = pacman.x
            new_y = pacman.y + 2
        elif mapp[pacman.x - 2][pacman.y] != 0:
            new_x = pacman.x - 2
            new_y = pacman.y
        elif mapp[pacman.x][pacman.y - 2] != 0:
            new_x = pacman.x
            new_y = pacman.y - 2
        return new_x, new_y

    def get_vector(self, new_x, new_y, blinky):
        vector = [0, 0]
        # 2*вектор блики
        vector[0] = 2 * (new_x - blinky.x)
        vector[1] = 2 * (new_y - blinky.y)
        return vector

    def get_route(self, pacman, blinky, mapp):

        # 2 точки после пакмана
        new_x, new_y = self.check_points(pacman, blinky, mapp)
        # 2*вектор блики
        vector = self.get_vector(new_x, new_y, blinky)
        # нахождение клетки с проходом
        if mapp[vector[0]][vector[1]] != 0:
            return vector
        else:
            if mapp[vector[0] + 1][vector[1]] == 1:
                vector[0] += 1
            elif mapp[vector[0] - 1][vector[1]] == 1:
                vector[0] -= 1
            elif mapp[vector[0]][vector[1] + 1] == 1:
                vector[1] += 1
            elif mapp[vector[0]][vector[1] - 1] == 1:
                vector[1] -= 1
            return vector

    def process_draw(self):
        self.game.screen.blit(self.image, self.rect)
