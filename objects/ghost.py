from typing import List
from math import sqrt

import pygame

from misc import get_ghost_path
from .character import CharacterObject


class GhostBase(CharacterObject):
    filenames: List[str] = [
        get_ghost_path('blue', 'up1.png'),
        get_ghost_path('blue', 'down1.png'),
        get_ghost_path('blue', 'left1.png'),
        get_ghost_path('blue', 'right1.png'),
        get_ghost_path('crazy_ghost', '1.png')
    ]
    filename: str = filenames[1]

    up_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[0]), (17, 17))
    down_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[1]), (17, 17))
    left_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[2]), (17, 17))
    right_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[3]), (17, 17))
    scared_img_resized: pygame.Surface = pygame.transform.scale(pygame.image.load(filenames[4]), (17, 17))

    def __init__(self, game, x, y) -> None:
        super().__init__(game, x, y)
        self.image = self.up_img_resized
        self.status = 'normal'
        self.obj_type = 'ghost'
        self.direction = "LEFT"
        self.speed[0] = 0
        self.speed[1] = 0

    def get_type(self) -> str:
        return self.obj_type

    def move(self, status,point_i: int = 0, point_j: int = 0) -> None:
        cell = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.cell_height
        y_plane = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.rect.y
        x_plane = self.game.scenes[self.game.MAIN_SCENE_INDEX].field.rect.x

        x_ghplane = self.rect.x - x_plane
        y_ghplane = self.rect.y - y_plane

        allowed = True
        if y_ghplane == cell * 14 and (x_ghplane < cell * 5 or x_ghplane > cell * 22):
            allowed = False

        if self.rect.x < x_plane:
            self.rect.x = x_plane + cell * len(self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[0]) - 18
        if self.rect.x > x_plane + cell * len(self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[0]) - 17:
            self.rect.x = x_plane

        ways = [10000,10000,10000,10000]
        if x_ghplane % cell == 0 and y_ghplane % cell == 0 and allowed:
            i_gh = int(y_ghplane / cell)
            j_gh = int(x_ghplane / cell)
            if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[y_ghplane // 17][x_ghplane // 17] == 4:
                #print(i_gh, j_gh)
                #self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[0][0] = 4
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh + 1][j_gh] != 0:
                    if self.direction != "UP":
                        way = round(sqrt(pow(point_i * cell - y_ghplane - cell,2) + pow(point_j * cell - x_ghplane, 2)), 3)
                        ways[0] = way
                        #print("D.", way)
                else: ways[0] = 100000
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh][j_gh + 1] != 0:
                    if self.direction != "LEFT":
                        way = round(sqrt(pow(point_i * cell -  y_ghplane, 2) + pow(point_j * cell - x_ghplane - cell, 2)), 3)
                        ways[1] = way
                        #print("R.", way)
                else: ways[1] = 100000
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh - 1][j_gh] != 0:
                    if self.direction != "DOWN":
                        way = round(sqrt(pow(point_i * cell - y_ghplane + cell, 2) + pow(point_j * cell - x_ghplane, 2)), 3)
                        ways[2] = way
                        #print("U.", way)
                else: ways[2] = 100000
                if self.game.scenes[self.game.MAIN_SCENE_INDEX].field.field[i_gh][j_gh - 1] != 0:
                    if self.direction != "RIGHT":
                        way = round(sqrt(pow(point_i * cell - y_ghplane, 2) + pow(point_j * cell - x_ghplane + cell, 2)), 3)
                        ways[3] = way
                        #print("L.", way)
                else: ways[3] = 100000

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

    def process_logic(self) -> None:
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

        if self.status == "normal":
            point_i = int((self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.rect.y - self.game.scenes[self.game.MAIN_SCENE_INDEX].field.rect.y) / self.game.scenes[self.game.MAIN_SCENE_INDEX].field.cell_height)
            point_j = int((self.game.scenes[self.game.MAIN_SCENE_INDEX].pacman.rect.x - self.game.scenes[self.game.MAIN_SCENE_INDEX].field.rect.x) / self.game.scenes[self.game.MAIN_SCENE_INDEX].field.cell_width)
        #print(point_i,point_j)

        self.move(self.status, 14, 24) #в аргументы точку куда идти(self.status, i,j)
