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

    def portal_event(self):
        left_border, right_border = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.get_borders()
        if self.rect.x < left_border:
            self.rect.x = right_border - 17
        elif self.rect.x > right_border - 17:
            self.rect.x = left_border
