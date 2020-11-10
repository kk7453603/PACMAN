import pygame

from objects.text import TextObject
from constants import Color
from objects.base import DrawableObject


class TableObject(DrawableObject):
    def __init__(self, game,
                 title: str = None,
                 title_color: Color = Color.WHITE,
                 title_is_bold: bool = True,
                 values: list = {},
                 header_color: Color = Color.RED,
                 header_is_italic: bool = True,
                 text_color: Color = Color.RED,
                 width: int = 200, height: int = 500,
                 x: int = 100, y: int = 100) -> None:
        super().__init__(game)
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.title = title
        self.title_color = title_color
        self.title_is_bold = title_is_bold
        self.header_color = header_color
        self.header_is_italic = header_is_italic
        self.text_color = text_color
        self.update_table(values)

    def update_table(self, values: list) -> None:
        self.cells = []
        for value in values:
            self.cells.append([value] + [str(val) for val in values[value]])
        self.texts_list = [[TextObject(game=self.game,
                                       text=self.title, is_bold=self.title_is_bold, color=self.title_color,
                                       x=self.rect.centerx, y=self.rect.y + 20)]]
        print(self.rect.centerx, self.rect.x // 2)
        for (i, column) in enumerate(self.cells):
            self.texts_list.append([])
            for (j, cell) in enumerate(column):
                self.texts_list[i].append(TextObject(game=self.game, text=cell,
                                                     is_bold=False,
                                                     color=self.header_color if j == 0 else self.text_color,
                                                     is_italic=self.header_is_italic if j == 0 else False,
                                                     x=self.rect.x + self.rect.width // 6 * (2 * i + 1),
                                                     y=self.rect.y + 55 + 30 * j))

    def process_draw(self) -> None:
        for texts in self.texts_list:
            for text in texts:
                text.process_draw()
