import pygame

from misc import get_nonzero_random_value
from objects.image import ImageObject


class CharacterObject(ImageObject):
    MAX_SPEED = 2

    def __init__(self, game, x: int = 0, y: int = 0, speed: int = None) -> None:
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed if speed else [
            get_nonzero_random_value(CharacterObject.MAX_SPEED),
            get_nonzero_random_value(CharacterObject.MAX_SPEED)
        ]

    def collides_with(self, other) -> bool:
        return pygame.sprite.collide_circle(self, other)