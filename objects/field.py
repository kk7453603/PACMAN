import pygame

from objects.base import DrawableObject
from fields.default import fieldArr
from constants import Color


class FieldObject(DrawableObject):
    field = fieldArr

    def __init__(self, game, x, y):
        super().__init__(game)
        self.x = x
        self.y = y

    def process_draw(self) -> None:

        y = self.y
        for (i, row) in enumerate(self.field):
            x = self.x
            for (j, cell) in enumerate(row):
                if cell == 0:
                    color = Color.BLUE
                elif cell == 1:
                    color = Color.BLACK
                elif cell == 2:
                    color = Color.BLACK
                pygame.draw.rect(self.game.screen, color, (x, y, 15, 15))
                x += 15
            y += 15
