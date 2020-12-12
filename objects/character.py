import pygame

from misc import get_nonzero_random_value
from objects.image import ImageObject


class CharacterObject(ImageObject):
    MAX_SPEED = 2

    def __init__(self, game, x: int = 0, y: int = 0, speed: int = None) -> None:
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.def_pos = (x, y)
        self.speed = speed if speed else [
            get_nonzero_random_value(CharacterObject.MAX_SPEED),
            get_nonzero_random_value(CharacterObject.MAX_SPEED)
        ]

    def move_to_default(self):
        print(self.rect)
        print('Go to default pos {}'.format(self.def_pos))
        print(self.rect)
        self.rect.x = self.def_pos[0]
        self.rect.y = self.def_pos[1]
        # self.move(self.def_pos[0], self.def_pos[1])

    def collides_with(self, other) -> bool:
        return pygame.sprite.collide_circle(self, other)

    def portal_event(self):
        left_border, right_border, cell = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.get_borders_cell()
        if self.rect.x < left_border:
            self.rect.x = right_border - cell
        elif self.rect.x > right_border - cell:
            self.rect.x = left_border
