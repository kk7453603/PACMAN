import pygame

from objects.character import CharacterObject
from fields.default import fieldArr


class PacmanObject(CharacterObject):
    filename = 'images/pacman.png'

    def __init__(self, game, x: int = 0, y: int = 0) -> None:
        # self.rect = self.image.get_rect()
        super().__init__(game, x, y)
        self.image_copy = pygame.transform.scale(pygame.image.load(self.filename), (16, 16))
        self.image = self.image_copy
        self.rect = self.image.get_rect()
        self.rotated_image = self.image_copy
        self.rect.x = x
        self.rect.y = y
        self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
        self.direction = "NONE"
        self.angle = 0
        self.speed[0] = 0
        self.speed[1] = 0
        self.radius = self.rect.width // 2
        self.obj_type = "pacman"

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and fieldArr[self.pos_on_field[1] - 1][self.pos_on_field[0]] != 0:
                self.direction = "UP"
                self.angle = 270
                self.speed[0] = 0
                self.speed[1] = -2
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and fieldArr[self.pos_on_field[1] + 1][self.pos_on_field[0]] != 0:
                self.direction = "DOWN"
                self.angle = 90
                self.speed[0] = 0
                self.speed[1] = 2
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and fieldArr[self.pos_on_field[1]][self.pos_on_field[0] - 1] != 0:
                self.direction = "LEFT"
                self.angle = 0
                self.speed[0] = -2
                self.speed[1] = 0
            elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and fieldArr[self.pos_on_field[1]][self.pos_on_field[0] + 1] != 0:
                self.direction = "RIGHT"
                self.angle = 180
                self.speed[0] = 2
                self.speed[1] = 0

    def rotate_image(self) -> None:
        self.rotated_image = self.image_copy
        if self.direction == "RIGHT":
            self.rotated_image = pygame.transform.flip(self.rotated_image, True, False)
        else:
            self.rotated_image = pygame.transform.rotate(self.rotated_image, self.angle)
            self.rect = self.rotated_image.get_rect(center=self.rect.center)
        self.image = self.rotated_image

    def get_type(self) -> str:
        return self.obj_type

    def move_to_direction(self) -> None:
        if self.direction == "UP":
            if fieldArr[self.pos_on_field[1]][self.pos_on_field[0]] == 0:
                self.rect.y = (self.pos_on_field[1] + 1) * 17 + 35 + 2
                self.pos_on_field[1] += 1
                self.direction = None
            self.rect.x = self.pos_on_field[0] * 17 + 70 + 2
            if (self.rect.y + self.speed[1]) % 17 >= 1:
                self.rotate_image()
                self.portal_event()
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
                self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
            elif fieldArr[self.pos_on_field[1] - 1][self.pos_on_field[0]] != 0:
                self.rotate_image()
                self.portal_event()
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
                self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
        elif self.direction == "DOWN":
            self.rect.x = self.pos_on_field[0] * 17 + 70
            if (self.rect.y + self.speed[1] + self.rect.height) % 17 < 2:
                self.rotate_image()
                self.portal_event()
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
                self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
            elif fieldArr[self.pos_on_field[1] + 1][self.pos_on_field[0]] != 0:
                self.rotate_image()
                self.portal_event()
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
                self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
        elif self.direction == "LEFT":
            self.rect.y = self.pos_on_field[1] * 17 + 35 + 2
            if (self.rect.x + self.speed[0]) % 17 > 1:
                self.rotate_image()
                self.portal_event()
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
                self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
            elif fieldArr[self.pos_on_field[1]][self.pos_on_field[0] - 1] != 0:
                self.rotate_image()
                self.portal_event()
                self.rect.x += self.speed[0]
                self.rect.y += self.speed[1]
                self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
        elif self.direction == "RIGHT":
            if fieldArr[self.pos_on_field[1]][self.pos_on_field[0] + 1] != 0:
                self.rect.y = self.pos_on_field[1] * 17 + 35 + 2
                if (self.rect.x + self.speed[0]) % 17 > 1:
                    self.rotate_image()
                    self.portal_event()
                    self.rect.x += self.speed[0]
                    self.rect.y += self.speed[1]
                    self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]
                elif fieldArr[self.pos_on_field[1]][self.pos_on_field[0]] != 0:
                    self.rotate_image()
                    self.portal_event()
                    self.rect.x += self.speed[0]
                    self.rect.y += self.speed[1]
                    self.pos_on_field = [(self.rect.x - 70) // 17, (self.rect.y - 35) // 17]

    def process_logic(self) -> None:
        self.move_to_direction()

    def collect_seed(self, seeds, score):
        for i in seeds:
            if self.collides_with(i) and i.get_type() == "seed":
                if i.is_available() and i.get_seed_type() == 0:
                    i.collected()
                    i.disappearing()
                    score.seed_eaten()
                elif i.is_available() and i.get_seed_type() == 1:
                    i.collected()
                    i.disappearing()
                    score.energizer_eaten()
