from constants import Color
from objects import ButtonObject
from objects import TableObject
from scenes import BaseScene


class HighScoreMenuScene(BaseScene):
    def create_objects(self) -> None:
        self.highscore = {
            'Jack': 5000,
            'Rechnoi': 4500,
            'Ann': 3300,
            'Robert': 3100,
            'August': 3050,
            'Ell': 2800,
            'Elsa': 2000,
            'S1mple': 1500,
            'Bob': 1300,
            'Noob': 5
        }
        self.highscore_table = TableObject(
            game=self.game,
            title='10 лучших результатов',
            values={
                'Место': [i for i in range(1, len(self.highscore) + 1)],
                'Имя': [key for key in self.highscore.keys()],
                'Очки': [value for value in self.highscore.values()]
            },
            header_color = Color.BLUE,
            text_color = Color.BLUE,
            x=self.game.WIDTH//2 - 250, y=20,
            width=500, height=400

        )
        self.button_back = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT - 50 - 25, 200, 50,
            Color.BLACK, self.back_to_menu, 'НАЗАД'
        )
        self.objects = [self.highscore_table, self.button_back]

    def back_to_menu(self) -> None:
        self.game.set_scene(self.game.MENU_SCENE_INDEX)

    def on_window_resize(self) -> None:
        self.button_back.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT - 50 - 25)
