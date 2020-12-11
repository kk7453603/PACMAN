import pygame

from objects.character import CharacterObject


class CherryObject(CharacterObject):
    filename = 'images/map/fruits/cherry.png'

    def __init__(self, game, x: int = 0, y: int = 0):
        self.inv_pic = pygame.transform.scale(pygame.image.load("images/map/inv_point.png"), (2, 2))
        self.vis_pic = pygame.transform.scale(pygame.image.load(self.filename), (10, 10))
        self.image = self.vis_pic
        self.rect = self.image.get_rect()
        self.ticks = 0
        self.checked = False
        super().__init__(game, x, y)
        self.isAvailable = False
        self.isCollected = False
        self.temp_available = False
        self.obj_type = "cherry"
        self.availability_pic()
        self.cherries = 0

    def get_type(self) -> str:
        return self.obj_type

    def disappearing(self) -> None:
        if self.isCollected == True and self.isAvailable == True:
            self.isAvailable = False
            self.filename = "images/map/inv_point.png"
            self.image = pygame.transform.scale(pygame.image.load(self.filename), (2, 2))

    def availability_pic(self):
        if self.isAvailable == True:
            self.image = self.vis_pic
        elif self.isAvailable == False:
            self.image = self.inv_pic

    def check_ticks(self):
        if self.ticks >=222:
            self.ticks = 0
            self.temp_available = False
        if self.temp_available == True:
           self.ticks+=1

    def available_check(self,score):
        self.check_ticks()

        if score.get_score() == 370 and not self.isAvailable and not self.checked:
            self.isAvailable = True
            self.isCollected = False
            self.temp_available = True
            self.checked = True

        elif not self.temp_available:
            self.isAvailable = False
            self.isCollected = True
            if score.get_score() != 370:
                self.checked = False
        self.availability_pic()

    def is_available(self) -> bool:
        return self.isAvailable

    def collected(self):
        self.cherries +=1
        self.isCollected = True
        self.temp_available = False
