import pygame

from objects.lives import LivesObject
from objects.seed import SeedObject


class NewLevel:
    def __init__(self, game) -> None:
        self.level = 0
        self.increase_speed = 1.05
        self.speed = 2

    def new_level(self, lives, seed):
        if seed.is_available():
            self.level += 1
            self.speed *= self.increase_speed
            lives.process_draw()
            #Character.speed = self.speed
            #Ghosts in center
            #seed process_draw()
