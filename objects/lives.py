import pygame

from objects.image import ImageObject


class LivesObject(ImageObject):
    filename = 'images/pacman/pacman_anime/left.png'
    image = pygame.image.load(filename)

    def __init__(self, game, x: int = 0, y: int = 0, num: int = 3):
        super().__init__(game)
        self.rect.x = x
        self.rect.y = y
        self.num = num

    def reduce_lives(self) -> None:
        # функция выполняется при коллизии пакмана с призраком
        if self.num > 0:
            self.num -= 1
        if self.num == 0:
            # код перехода в меню проигрыша
            pass

    def process_draw(self) -> None:
        for life in range(self.num):
            self.process_draw()
            self.rect.x += self.rect.width + 20
