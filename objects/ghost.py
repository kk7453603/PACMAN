import pygame
from collections import deque

from .character import CharacterObject
from fields.default import fieldArr


def matrix_edit_for_bfs(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = 1 - graph[i][j]
    return graph


def coordinates_validation(graph, x, y):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[x]):
        return False
    return graph[x][y] != 1


def bfs(graph, start, end):
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, 1, -1]
    visited = {}
    Q = deque([start])
    dist = {start: 0}
    while len(Q):
        curPoint = Q.popleft()
        curDist = dist[curPoint]
        for dx, dy in zip(delta_x, delta_y):
            nextPoint = (curPoint[0] + dx, curPoint[1] + dy)
            if nextPoint not in visited and nextPoint not in visited.values():
                visited[nextPoint] = curPoint
            if not coordinates_validation(graph, nextPoint[0], nextPoint[1]) or nextPoint in dist.keys():
                continue
            dist[nextPoint] = curDist + 1
            Q.append(nextPoint)
            if nextPoint == end:
                visited[nextPoint] = curPoint
                return visited


class GhostBase(CharacterObject):
    up_filename = 'images/ghost/blue/up1.png'
    down_filename = 'images/ghost/blue/down1.png'
    left_filename = 'images/ghost/blue/left1.png'
    right_filename = 'images/ghost/blue/right1.png'
    scared_filename = 'images/ghost/crazy_ghost/1.png'
    eyes_up_filename = 'images/eyes/eyes_up.png'
    eyes_down_filename = 'images/eyes/eyes_down.png'
    eyes_right_filename = 'images/eyes/eyes_right.png'
    eyes_left_filename = 'images/eyes/eyes_left.png'
    filename = down_filename

    filenames = [up_filename, down_filename, left_filename, right_filename, scared_filename, eyes_up_filename,
                 eyes_down_filename, eyes_left_filename, eyes_right_filename]

    up_img = pygame.image.load(filenames[0])
    down_img = pygame.image.load(filenames[1])
    left_img = pygame.image.load(filenames[2])
    right_img = pygame.image.load(filenames[3])
    scared_img = pygame.image.load(filenames[4])
    eyes_up_img = pygame.image.load(filenames[5])
    eyes_down_img = pygame.image.load(filenames[6])
    eyes_left_img = pygame.image.load(filenames[7])
    eyes_right_img = pygame.image.load(filenames[8])

    up_img_resized = pygame.transform.scale(up_img, (15, 15))
    down_img_resized = pygame.transform.scale(down_img, (15, 15))
    left_img_resized = pygame.transform.scale(left_img, (15, 15))
    right_img_resized = pygame.transform.scale(right_img, (15, 15))
    scared_img_resized = pygame.transform.scale(scared_img, (15, 15))
    eyes_up_img_resized = pygame.transform.scale(eyes_up_img, (15, 15))
    eyes_down_img_resized = pygame.transform.scale(eyes_down_img, (15, 15))
    eyes_left_img_resized = pygame.transform.scale(eyes_left_img, (15, 15))
    eyes_right_img_resized = pygame.transform.scale(eyes_right_img, (15, 15))

    def __init__(self, game, x, y) -> None:
        super().__init__(game)
        self.down_down = False
        self.image = self.up_img_resized
        self.status = 'normal'
        self.movement_slow_down = 10
        self.keyboard_input_movement_sec = 1
        self.moving_home_sec = 0
        self.processing_cell = 0
        self.pos_on_field = []
        cell_y = 105
        for i in range(len(fieldArr)):
            cell_x = 150
            self.pos_on_field.append([])
            for j in range(len(fieldArr[i])):
                cell_type = fieldArr[i][j]
                self.pos_on_field[i].append([cell_x, cell_y, cell_type])
                cell_x += 15
            cell_y += 15
        self.cell = [14, 13]
        self.rect.x = self.pos_on_field[self.cell[0]][self.cell[1]][0]
        self.rect.y = self.pos_on_field[self.cell[0]][self.cell[1]][1]
        self.pressed = None
        self.matrix_copy_for_graph = [[k if k != 2 else 1 for k in i] for i in fieldArr]
        self.graph = matrix_edit_for_bfs(self.matrix_copy_for_graph)
        self.path = None
        self.moving_home = None

    def test_move(self, status):
        self.keyboard_input_movement_sec += 1
        if self.keyboard_input_movement_sec % self.movement_slow_down == 0:
            if self.pressed == 'left':
                if self.pos_on_field[self.cell[0]][self.cell[1] - 1][2] != 0:
                    self.cell[1] -= 1
                    self.rect.x = self.pos_on_field[self.cell[0]][self.cell[1]][0]
                if self.status == 'normal':
                    self.image = self.left_img_resized
            elif self.pressed == 'right':
                if self.pos_on_field[self.cell[0]][self.cell[1] + 1][2] != 0:
                    self.cell[1] += 1
                    self.rect.x = self.pos_on_field[self.cell[0]][self.cell[1]][0]
                if self.status == 'normal':
                    self.image = self.right_img_resized
            elif self.pressed == 'down':
                if self.pos_on_field[self.cell[0] + 1][self.cell[1]][2] != 0:
                    self.cell[0] += 1
                    self.rect.y = self.pos_on_field[self.cell[0]][self.cell[1]][1]
                if self.status == 'normal':
                    self.image = self.down_img_resized
            elif self.pressed == 'up':
                if self.pos_on_field[self.cell[0] - 1][self.cell[1]][2] != 0:
                    self.cell[0] -= 1
                    self.rect.y = self.pos_on_field[self.cell[0]][self.cell[1]][1]
                if self.status == 'normal':
                    self.image = self.up_img_resized

    def get_path_to_home(self):
        visited = bfs(self.graph, (self.cell[0], self.cell[1]), (14, 13))
        path = []
        previous_cell = 14, 13
        rent_cell = visited[previous_cell]
        path.append(previous_cell)
        while True:
            path.append(rent_cell)
            rent_cell = visited[previous_cell]
            previous_cell = rent_cell
            if rent_cell == (self.cell[0], self.cell[1]):
                break
        path.reverse()
        self.path = path

    def move_home(self):
        self.pressed = None
        self.image = self.eyes_up_img_resized
        path = self.path
        self.moving_home_sec += 1
        if self.moving_home_sec % self.movement_slow_down == 0:
            self.rect.x = self.pos_on_field[path[self.processing_cell][0]][path[self.processing_cell][1]][0]
            self.rect.y = self.pos_on_field[path[self.processing_cell][0]][path[self.processing_cell][1]][1]
            self.processing_cell += 1
            if self.processing_cell == len(path):
                self.image = self.up_img_resized
                self.processing_cell = 0
                self.moving_home = False
                self.__init__(self.game, 345, 300)

    def check_move(self):
        if self.moving_home:
            self.get_path_to_home()
            self.move_home()

    def process_logic(self) -> None:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        self.test_move(self.status)
        self.check_move()

        # При нажатии X приведение переходит в состояние испуга
        if keys[pygame.K_x]:
            self.status = 'scared'

        if self.status == 'scared' and self.moving_home != True:
            self.image = self.scared_img_resized

    def process_draw(self) -> None:
        self.game.screen.blit(self.image, self.rect)
