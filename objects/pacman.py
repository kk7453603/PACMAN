import pygame

from objects.character import CharacterObject
from fields.default import fieldArr


class PacmanObject(CharacterObject):
    filename = 'images/pacman/pacman_anime/close.png'
    image_copy = pygame.image.load(filename)
    image = pygame.transform.scale(image_copy, (15, 15))

    def __init__(self, game, x: int = 0, y: int = 0) -> None:
        super().__init__(game, x, y)
        self.rotated_image = self.image_copy
        self.direction = "NONE"
        self.angle = 0
        self.speed[0] = 0
        self.speed[1] = 0
        self.radius = self.rect.width // 2

        self.tick = 10
        self.sec = 1

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
        self.cell = [23, 13]
        self.rect.x = self.pos_on_field[self.cell[0]][self.cell[1]][0]
        self.rect.y = self.pos_on_field[self.cell[0]][self.cell[1]][1]
        self.pressed = 'none'

    def rotate_image(self):
        self.rotated_image = self.image_copy
        if self.direction == "RIGHT":
            self.rotated_image = pygame.transform.flip(self.rotated_image, True, False)
        else:
            self.rotated_image = pygame.transform.rotate(self.rotated_image, self.angle)
            self.rect = self.rotated_image.get_rect(center=self.rect.center)
        self.image = self.rotated_image

    def move_to_direction(self):
        self.sec += 2
        if self.sec % self.tick == 1:
            if self.pressed == 'left':
                if self.pos_on_field[self.cell[0]][self.cell[1] - 1][2] != 0:
                    self.cell[1] -= 1
                    self.rect.x = self.pos_on_field[self.cell[0]][self.cell[1]][0]
            elif self.pressed == 'right':
                if self.pos_on_field[self.cell[0]][self.cell[1] + 1][2] != 0:
                    self.cell[1] += 1
                    self.rect.x = self.pos_on_field[self.cell[0]][self.cell[1]][0]
            elif self.pressed == 'down':
                if self.pos_on_field[self.cell[0] + 1][self.cell[1]][2] != 0:
                    self.cell[0] += 1
                    self.rect.y = self.pos_on_field[self.cell[0]][self.cell[1]][1]
            elif self.pressed == 'up':
                if self.pos_on_field[self.cell[0] - 1][self.cell[1]][2] != 0:
                    self.cell[0] -= 1
                    self.rect.y = self.pos_on_field[self.cell[0]][self.cell[1]][1]

    def process_logic(self) -> None:
        self.move_to_direction()

    def collect_seed(self, seeds, score):
        for i in seeds:
            if self.collides_with(i) and i.is_available():
                i.collected()
                i.disappearing()
                score.seed_eaten()

    def process_draw(self) -> None:
        self.game.screen.blit(self.image, self.rect)
