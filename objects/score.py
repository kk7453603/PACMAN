import pygame


class ScoreObject:
    def __init__(self):
        self.score = 0
        self.point_for_seed = 10
        self.point_for_energizer = 50
        self.point_for_ghost = 200

    def seed_eaten(self):
        self.score += self.point_for_seed

    def energizer_eaten(self):
        self.score += self.point_for_energizer

    def ghost_eaten(self):
        self.score += self.point_for_ghost
        self.point_for_ghost *= 2
        if self.point_for_ghost == 3200:
            self.point_for_ghost = 200

    def starting_new_lvl(self):
        self.point_for_seed = 10
        self.point_for_ghost = 200

    def draw(self):
        print('score = ', self.score)
        #Вывод надо будет изменить в соответствие со шрифтом, координатами и всем прочим, сейчас тестовая версия
