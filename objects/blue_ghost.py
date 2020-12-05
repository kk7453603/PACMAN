import pygame

from .character import CharacterObject
from .ghost import GhostBase


class Blue_ghost(GhostBase):
    def __init__(self):
        super().__init__()

    def get_route(self, pacman, blinky, mapp):
        vector = [0, 0]
        # 2 точки после пакмана
        if mapp[pacman.x + 2][pacman.y] != 0:
            new_x = pacman.x + 2
            new_y = pacman.y
        else:
            new_x = pacman.x
            new_y = pacman.y + 2
        # 2*вектор блики
        vector[0] = 2 * (new_x - blinky.x)
        vector[1] = 2 * (new_y - blinky.y)
        # нахождение клетки с проходом
        if mapp[vector[0]][vector[1]]!=0:
            return vector
        else:
            if mapp[vector[0]+1][vector[1]]==1:
                vector[0]+=1
            elif mapp[vector[0]-1][vector[1]]==1:
                vector[0]-=1
            elif mapp[vector[0]][vector[1]+1]==1:
                vector[1]+=1
            elif mapp[vector[0]][vector[1]-1]==1:
                vector[1]-=1
            return vector
