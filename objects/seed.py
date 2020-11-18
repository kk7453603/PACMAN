import pygame

from .image import ImageObject


class SeedObject:
    
    def __init__(self, game, type):
        super().__init__(game)
        self.isAvailable = True
        self.type = type
        self.isCollected = False
        if type == 0:
            filename = 'images/map/point.png'
        else:
            filename = 'images/map/tablet.png'
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

    def disappearing(self):
        if self.isCollected == True and self.isAvailable == True:
            self.isAvailable = False
            filename = "images/map/inv_point.png"
            self.image = pygame.image.load(filename)
    def is_available(self) -> bool:
        return self.isAvailable

    def collected(self):
        self.isCollected = True
