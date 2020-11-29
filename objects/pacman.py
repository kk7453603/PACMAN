import pygame

from objects.character import CharacterObject

class PacmanObject(CharacterObject):
    filename = 'images/pacman.png'
    image_copy = pygame.image.load(filename)

    def __init__(self, game, x: int = 0, y: int = 0) -> None:
        super().__init__(game, x, y)
        image_copy = pygame.transform.scale(self.image_copy, (17, 17))
        self.image = image_copy
        # self.image_copy = self.image
        self.rotated_image = self.image_copy
        self.direction = "NONE"
        self.angle = 0
        self.speed[0] = 0
        self.speed[1] = 0
        self.radius = self.rect.width // 2
        #self.left_border = self.game.scenes[1].field.rect.x
        #self.right_border = self.game.scenes[1].field.rect.x + self.game.scenes[1].field.cell_width
        self.left_border = 150
        self.right_border = 626

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.direction = "UP"
                self.angle = 270
                self.speed[0] = 0
                self.speed[1] = -2
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.direction = "DOWN"
                self.angle = 90
                self.speed[0] = 0
                self.speed[1] = 2
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.direction = "LEFT"
                self.angle = 0
                self.speed[0] = -2
                self.speed[1] = 0
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
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

    def move_to_direction(self) -> None:
        # self.rotate_image()
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.x < self.left_border:
            self.rect.x = self.right_border - 10
        elif self.rect.x > self.right_border - 10:
            self.rect.x = self.left_border

    def process_logic(self) -> None:
        self.move_to_direction()

    def collect_seed(self, seeds, score):
        for i in seeds:
            if self.collides_with(i) and i.is_available():
                i.collected()
                i.disappearing()
                score.seed_eaten()
