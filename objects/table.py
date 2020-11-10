from objects.text import TextObject
from constants import Color
from objects.base import DrawableObject


class TableObject(DrawableObject):
    def __init__(self, game,
                 title: str = None,
                 values: list = {},
                 x: int = 100, y: int = 100) -> None:
        super().__init__(game)
        self.x = x
        self.y = y
        self.title = title
        self.color = Color.WHITE;
        self.update_table(values)

    def update_table(self, values: list) -> None:
        self.cells = []
        for value in values:
            self.cells.append([value] + [str(val) for val in values[value]])
        self.texts_list = [[TextObject(game=self.game, text=self.title, color=Color.WHITE, x=self.x+70, y=self.y)]]
        for (i, column) in enumerate(self.cells):
            self.texts_list.append([])
            for (j, cell) in enumerate(column):
                self.texts_list[i].append(TextObject(game=self.game, text=cell, color=Color.RED,
                                                    x=self.x + 150 * i,
                                                    y=self.y + 40 + 30 * j))

    def process_draw(self) -> None:
        for texts in self.texts_list:
            for text in texts:
                text.process_draw()
