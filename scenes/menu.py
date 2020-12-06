import pygame

from constants import Color
from objects import ButtonObject
from scenes import BaseScene


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (800,600))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Logo(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (300,100))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class MenuScene(BaseScene):
    def create_objects(self) -> None:
        self.button_start = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 - 175, 200, 50,
            Color.BLACK, self.start_game, "ЗАПУСК ИГРЫ"
        )
        self.button_high_score_menu = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 - 75, 200, 50,
            Color.BLACK, self.open_high_score_menu, "РЕКОРДЫ"
        )
        self.button_exit = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 + 125, 200, 50,
            Color.BLACK, self.game.exit_game, 'ВЫХОД'
        )
        self.button_settings = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 + 25, 200, 50,
            Color.BLACK, self.open_settings, 'НАСТРОЙКИ'
        )
        self.objects = [self.button_start, self.button_high_score_menu, self.button_exit, self.button_settings]

    def start_game(self) -> None:
        self.game.set_scene(self.game.MAIN_SCENE_INDEX)

    def open_high_score_menu(self) -> None:
        self.game.set_scene(self.game.HIGH_SCORE_MENU_SCENE_INDEX)

    def open_settings(self) -> None:
        self.game.set_scene(self.game.SETTINGS_INDEX)

    def on_window_resize(self) -> None:
        self.button_start.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 25 - 25 - 50)
        self.button_high_score_menu.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 25)
        self.button_exit.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 25 + 25)


    def additional_draw(self) -> None:
        self.background = Background('images/menu/background.jpg', [0, 0])
        self.logo = Logo('images/menu/pac-man_inscription.png', [140, 35])
        self.screen.blit(self.background.image, self.background.rect)
        self.screen.blit(self.logo.image, self.logo.rect)
