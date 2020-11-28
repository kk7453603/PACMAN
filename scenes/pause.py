import pygame

from constants import Color
from objects import TextObject
from scenes import BaseScene
from objects import ButtonObject


class PauseScene(BaseScene):
    def create_objects(self) -> None:
        self.text = TextObject(
            game=self.game,
            text='Меню паузы', color=Color.RED,
            x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2 - 200
        )
        self.button_resume = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 75, 200, 50,
            Color.RED, self.go_menu, "Продолжить"
        )
        self.button_restart = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2, 200, 50,
            Color.RED, self.start_game, "Заново"
        )
        self.button_menu = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 75, 200, 50,
            Color.RED, self.back_to_menu, "Меню"
        )

        self.objects.append(self.text)
        self.objects.append(self.button_resume)
        self.objects.append(self.button_menu)
        self.objects.append(self.button_restart)

    def start_game(self) -> None:
        self.game.set_scene(self.game.MAIN_SCENE_INDEX)

    def go_menu(self) -> None:
        self.game.set_scene(self.game.MAIN_SCENE_INDEX, resume=True)

    def go_resume(self) -> None:
        self.game.set_scene(self.game.MAIN_SCENE_INDEX, resume=False)

    def additional_event_check(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_scene(self.game.MAIN_SCENE_INDEX, resume=True)

    def on_window_resize(self) -> None:
        self.button_resume.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 20 - 25)

    def back_to_menu(self):
        self.game.set_scene(self.game.MENU_SCENE_INDEX, resume=True)
