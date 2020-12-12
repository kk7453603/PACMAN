import pygame

from objects.text import TextObject


class ScoreObject(TextObject):
    def __init__(self, game, color) -> None:
        super().__init__(game, color=color)
        self.score = 0
        self.point_for_seed = 10
        self.point_for_energizer = 50
        self.point_for_ghost = 200
        self.update_score()
        self.obj_type = "score"

    def get_type(self) -> str:
        return self.obj_type

    def cherry_eaten(self) -> None:
        self.score += self.point_for_energizer * 6
        self.update_score()

    def update_score(self) -> None:
        self.update_text(str(self.score))

    def seed_eaten(self) -> None:
        self.score += self.point_for_seed
        self.update_score()

    def energizer_eaten(self) -> None:
        self.score += self.point_for_energizer
        self.update_score()

    def ghost_eaten(self) -> None:
        self.score += self.point_for_ghost
        self.point_for_ghost *= 2
        if self.point_for_ghost == 3200:
            self.point_for_ghost = 200
        self.update_score()

    def starting_new_lvl(self) -> None:
        self.point_for_seed = 10
        self.point_for_ghost = 200

    def get_score(self) -> int:
        return self.score
