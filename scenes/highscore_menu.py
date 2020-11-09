from constants import Color
from objects import ButtonObject
from scenes import BaseScene


class HighScoreMenuScene(BaseScene):
    def create_objects(self) -> None:
        self.button_back = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 + 25, 200, 50,
            Color.RED, self.game.back_to_menu, 'Назад'
        )
        self.objects = [self.button_back]

    def start_game(self) -> None:
        self.game.set_scene(self.game.MENU_SCENE_INDEX)

    def on_window_resize(self) -> None:
        self.button_back.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT // 2 - 20 - 25)
