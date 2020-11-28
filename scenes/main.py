import pygame

from objects import FieldObject
from scenes import BaseScene


class MainScene(BaseScene):
    MAX_COLLISIONS = 15
    BALLS_COUNT = 3

    def create_objects(self) -> None:
        self.field = FieldObject(self.game, 10, 10, 17, 17)
        self.objects.append(self.field)

    def additional_event_check(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.PAUSE_SCENE_INDEX)
