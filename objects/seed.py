import pygame

from objects.character import CharacterObject


class SeedObject(CharacterObject):
    filename = 'images/map/point.png'

    def __init__(self, game, type ,x: int = 0, y: int = 0):
        self.type = type
        if self.type == 0:
            self.filename = 'images/map/point.png'
            self.image_copy = pygame.transform.scale(pygame.image.load(self.filename), (5, 5))
        elif self.type == 1:
            self.filename = 'images/map/tablet.png'
            self.image_copy = pygame.transform.scale(pygame.image.load(self.filename), (8, 8))
        self.image = self.image_copy
        self.rect = self.image.get_rect()
        super().__init__(game, x, y)
        self.isAvailable = True
        self.isCollected = False

    def disappearing(self) -> None:
        if self.isCollected == True and self.isAvailable == True:
            self.isAvailable = False
            self.filename = "images/map/inv_point.png"
            self.image = pygame.transform.scale(pygame.image.load(self.filename),(2,2))

    def is_available(self) -> bool:
        return self.isAvailable

    def collected(self):
        self.isCollected = True
