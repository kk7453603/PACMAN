import pygame

from .image import ImageObject


class SeedObject(ImageObject):
    def __init__(self, game, type):
        super().__init__(game)
        self.type = type
        if self.type == 0:
            self.filename = 'images/map/point.png'
        elif self.type == 1:
            self.filename = 'images/map/tablet.png'
        self.image = pygame.image.load(self.filename)
        self.rect = self.image.get_rect()
