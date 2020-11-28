import pygame

from .image import ImageObject


class SeedObject(ImageObject):
    def __init__(self, game, type):
        super().__init__(game)
        self.isAvailable = True
        self.type = type
        self.isCollected = False
        if self.type == 0:
            self.filename = 'images/map/point.png'
        elif self.type == 1:
            self.filename = 'images/map/tablet.png'
        self.image = pygame.image.load(self.filename)
        self.rect = self.image.get_rect()

    def disappearing(self) -> None:
        if self.isCollected == True and self.isAvailable == True:
            self.isAvailable = False
            self.filename = "images/map/inv_point.png"
            self.image = pygame.image.load(filename)

    def is_available(self) -> bool:
        return self.isAvailable

    def collected(self):
        self.isCollected = True
