import pygame

from .image import ImageObject


class SeedObject:
    
    def __init__(self, game, type):
        super().__init__(game)
        self.type = type
        self.isCollected = False
        if type == 0:
            filename = 'images/map/point.png'
        else:
            filename = 'images/map/tablet.png'
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

    def disappearing(self):
        if self.isCollected == True:
            filename = "images/map/inv_point.png"
            self.image = pygame.image.load(filename)

    def collected(self):
        self.isCollected = True
