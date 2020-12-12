from typing import List
from math import sqrt

import pygame

from misc import get_ghost_path, get_eyes_path
from .character import CharacterObject


class GhostBase(CharacterObject):
    filenames: List[str] = [
        get_ghost_path('blue', 'up1.png'),
        get_ghost_path('blue', 'down1.png'),
        get_ghost_path('blue', 'left1.png'),
        get_ghost_path('blue', 'right1.png'),
        get_ghost_path('crazy_ghost', '1.png'),
        get_eyes_path('death', 'up.png'),
        get_eyes_path('death', 'down.png'),
        get_eyes_path('death', 'left.png'),
        get_eyes_path('death', 'right.png')
    ]
    filename: str = filenames[1]

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (17, 17))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (17, 17))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (17, 17))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (17, 17))
    scared_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[4]), (17, 17))
    up_eyes_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[5]), (17, 17))
    down_eyes_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[6]), (17, 17))
    left_eyes_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[7]), (17, 17))
    right_eyes_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[8]), (17, 17))

    def __init__(self, game, x, y) -> None:
        super().__init__(game, x, y)
        self.start_x = x
        self.start_y = y
        self.image = self.up_img_resized
        self.status = 'normal'
        self.obj_type = 'ghost'
        self.direction = "LEFT"
        self.speed[0] = 0
        self.speed[1] = 0
        self.allowed = True
        self.die = False
        self.start_time = 0
        self.start_direction = 'LEFT'
        self.is_home = False

    def get_type(self) -> str:
        return self.obj_type

    def start_hunt(self, point_i, point_j, cell, x_ghplane, y_ghplane):
        self.direction = "UP"
        if y_ghplane == 11 * cell and x_ghplane == 13 * cell:
            way_l = round(sqrt(pow(point_i * cell - y_ghplane, 2) + pow(point_j * cell - x_ghplane + cell, 2)), 3)
            way_r = round(sqrt(pow(point_i * cell - y_ghplane, 2) + pow(point_j * cell - x_ghplane - cell, 2)), 3)
            if way_r > way_l:
                self.direction = "LEFT"
            else:
                self.direction = "RIGHT"
            self.allowed = True
            self.die = False

    def scare(self):
        self.status = 'scared'
        self.image = self.scared_img_resized
        self.start_time = pygame.time.get_ticks()

    def go_home(self) -> bool:
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.direction = self.start_direction
        self.is_home = True

    # self.move(self.status, 14, 24)  # в аргументы точку куда идти (self.status, i (это y), j (это x))
    def move(self, status, point_i: int = 0, point_j: int = 0) -> None:
        cell = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.cell_height
        y_plane = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.rect.y
        x_plane = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.rect.x
        x_ghplane = self.rect.x - x_plane
        y_ghplane = self.rect.y - y_plane
        self.allowed = True
        if x_ghplane == 13 * cell and y_ghplane == 13 * cell:
            self.start_hunt(point_i, point_j, cell, x_ghplane, y_ghplane)
        if self.die:
            self.allowed = False
            self.start_hunt(point_i, point_j, cell, x_ghplane, y_ghplane)
        if y_ghplane == cell * 14 and (x_ghplane < cell * 5 or x_ghplane > cell * 22):
            self.allowed = False
        if self.rect.x < x_plane:
            self.rect.x = x_plane + cell * len(self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[0]) - 18
        if self.rect.x > x_plane + cell * len(self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[0]) - 17:
            self.rect.x = x_plane
        ways = [10000, 10000, 10000, 10000]
        if x_ghplane % cell == 0 and y_ghplane % cell == 0 and self.allowed:
            i_gh = int(y_ghplane / cell)
            j_gh = int(x_ghplane / cell)
            if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[y_ghplane // 17][x_ghplane // 17] == 4:
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh + 1][j_gh] != 0:
                    if self.direction != "UP":
                        way = round(
                            sqrt(pow(point_i * cell - y_ghplane - cell, 2) + pow(point_j * cell - x_ghplane, 2)), 3)
                        ways[0] = way
                else:
                    ways[0] = 100000
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh][j_gh + 1] != 0:
                    if self.direction != "LEFT":
                        way = round(
                            sqrt(pow(point_i * cell - y_ghplane, 2) + pow(point_j * cell - x_ghplane - cell, 2)), 3)
                        ways[1] = way
                else:
                    ways[1] = 100000
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh - 1][j_gh] != 0:
                    if self.direction != "DOWN":
                        way = round(
                            sqrt(pow(point_i * cell - y_ghplane + cell, 2) + pow(point_j * cell - x_ghplane, 2)), 3)
                        ways[2] = way
                else:
                    ways[2] = 100000
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh][j_gh - 1] != 0:
                    if self.direction != "RIGHT":
                        way = round(
                            sqrt(pow(point_i * cell - y_ghplane, 2) + pow(point_j * cell - x_ghplane + cell, 2)), 3)
                        ways[3] = way
                else:
                    ways[3] = 100000
                minInd = ways.index(min(ways))
                if minInd == 0 and self.direction != "UP":
                    self.direction = "DOWN"
                elif minInd == 1 and self.direction != "LEFT":
                    self.direction = "RIGHT"
                elif minInd == 2 and self.direction != "DOWN":
                    self.direction = "UP"
                elif minInd == 3 and self.direction != "RIGHT":
                    self.direction = "LEFT"
            else:
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh + self.speed[1]][j_gh + self.speed[0]] == 0:
                    if self.speed[0]:
                        if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh - 1][j_gh]:
                            self.direction = "UP"
                        else:
                            self.direction = "DOWN"
                    else:
                        if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh][j_gh + 1]:
                            self.direction = "RIGHT"
                        else:
                            self.direction = "LEFT"
        if self.status == 'normal':
            if self.direction == "DOWN":
                self.image = self.down_img_resized
            elif self.direction == "UP":
                self.image = self.up_img_resized
            elif self.direction == "LEFT":
                self.image = self.left_img_resized
            elif self.direction == "RIGHT":
                self.image = self.right_img_resized

    def define_direction(self):
        if self.direction == "UP":
            self.speed[0] = 0
            self.speed[1] = -1
        if self.direction == "DOWN":
            self.speed[0] = 0
            self.speed[1] = 1
        if self.direction == "RIGHT":
            self.speed[0] = 1
            self.speed[1] = 0
        if self.direction == "LEFT":
            self.speed[0] = -1
            self.speed[1] = 0
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def scare_to_normal(self):
        if pygame.time.get_ticks() - self.start_time > 10000 or self.is_home:
            self.status = 'normal'
            self.is_home = False
