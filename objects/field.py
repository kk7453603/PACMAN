from typing import List

import pygame

from objects.base import DrawableObject
from fields.default import fieldArr
from constants import Color
from .seed import SeedObject


class FieldObject(DrawableObject):
    field = fieldArr

    def __init__(self, game, x: int = 0, y: int = 0, cell_width: int = 10, cell_height: int = 10) -> None:
        super().__init__(game)
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.rect = pygame.rect.Rect(x, y, self.cell_width * len(self.field[0]), self.cell_height * len(self.field))

    def get_pathways(self) -> List[pygame.rect.Rect]:
        pathways = []
        for (i, row) in enumerate(self.field):
            for (j, cell) in enumerate(row):
                if cell == '1':
                    x = self.rect.x + j * self.cell_width
                    y = self.rect.y + x * self.cell_height
                    pathways.append(pygame.rect.Rect(x, y, self.cell_width, self.cell_height))
        return pathways

    def get_walls(self) -> List[pygame.rect.Rect]:
        walls = []
        for (i, row) in enumerate(self.field):
            for (j, cell) in enumerate(row):
                if cell == '2':
                    x = self.rect.x + j * self.cell_width
                    y = self.rect.y + x * self.cell_height
                    walls.append(pygame.rect.Rect(x, y, self.cell_width, self.cell_height))
        return walls

    def process_draw(self) -> None:
        for (i, row) in enumerate(self.field):
            for (j, cell) in enumerate(row):
                if cell == 0:
                    color = Color.BLUE
                elif cell == 1 or 2:
                    color = Color.WHITE
                x = self.rect.x + self.cell_width * j
                y = self.rect.y + self.cell_height * i
                pygame.draw.rect(self.game.screen, color, (x, y, self.cell_width, self.cell_height))

    def add_seeds(self,obj):
        for (i, row) in enumerate(self.field):
            for (j, cell) in enumerate(row):
                if cell == 0:
                    pass
                elif cell == 2:
                    pass
                elif cell == 1:
                    x = self.rect.x + self.cell_width * j
                    y = self.rect.y + self.cell_height * i
                    x += 6
                    y += 6
                    # Смещаем,чтобы зерно было в центре клетки
                    obj.append(SeedObject(self.game,0,x,y))
        return obj
