import pygame

from .character import CharacterObject


class GhostBase(CharacterObject):
    up_filename = 'images/ghost/blue/up1.png'
    down_filename = 'images/ghost/blue/down1.png'
    left_filename = 'images/ghost/blue/left1.png'
    right_filename = 'images/ghost/blue/right1.png'
    scared_filename = 'images/ghost/crazy_ghost/1.png'
    filename = down_filename

    filenames = [up_filename, down_filename, left_filename, right_filename, scared_filename]

    up_img = pygame.image.load(filenames[0])
    down_img = pygame.image.load(filenames[1])
    left_img = pygame.image.load(filenames[2])
    right_img = pygame.image.load(filenames[3])
    scared_img = pygame.image.load(filenames[4])

    up_img_resized = pygame.transform.scale(up_img, (35, 35))
    down_img_resized = pygame.transform.scale(down_img, (35, 35))
    left_img_resized = pygame.transform.scale(left_img, (35, 35))
    right_img_resized = pygame.transform.scale(right_img, (35, 35))
    scared_img_resized = pygame.transform.scale(scared_img, (35, 35))

    def __init__(self, game) -> None:
        super().__init__(game)
        self.image = self.up_img_resized
        self.status = 'normal'

    def test_move(self, status) -> None:
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.rect.y += self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.down_img_resized
        elif keys[pygame.K_UP]:
            self.rect.y -= self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.up_img_resized
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.left_img_resized
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.MAX_SPEED
            if self.status == 'normal':
                self.image = self.right_img_resized

    def process_logic(self) -> None:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        self.test_move(self.status)

        # При нажатии X приведение переходит в состояние испуга
        if keys[pygame.K_x]:
            self.status = 'scared'
        else:
            self.status = 'normal'

        if self.status == 'scared':
            self.image = self.scared_img_resized

    def process_draw(self) -> None:
        self.game.screen.blit(self.image, self.rect)
