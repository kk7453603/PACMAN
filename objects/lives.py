import pygame

from objects.image import ImageObject
from objects.base import DrawableObject


class LivesObject(DrawableObject):
    filename = 'images/map/fruits/apple.png'

    def __init__(self, game, x: int = 0, y: int = 0, num: int = 3) -> None:
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.max = num
        self.num = self.max
        self.images = []
        self.obj_type = "lives"
        for i in range(num):
            self.images.append(
                ImageObject(
                    self.game,
                    self.filename,
                    self.rect.x,
                    self.rect.y))
            self.images[i].move(self.rect.x + 30 * i, self.rect.y)

    def reduce_lives(self) -> None:
        if self.num > 0:
            self.num -= 1
            self.images.pop()

    def get_type(self) -> str:
        return self.obj_type

    def get_lives_count(self) -> int:
        return self.num

    def get_max_lives_count(self) -> int:
        return self.max

    def get_live_status(self) -> bool:
        if self.num <= 0:
            return False
        return True

    def process_draw(self) -> None:
        for image in self.images:
            image.process_draw()
