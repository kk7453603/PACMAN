import pygame

from objects import FieldObject, PacmanObject, OrangeGhostObject, RedGhostObject
from objects import GhostBase
from constants import Color
from objects import TextObject, ScoreObject, LivesObject
from scenes import BaseScene


class MainScene(BaseScene):
    MAX_COLLISIONS = 15
    BALLS_COUNT = 3

    def create_objects(self) -> None:
        self.nickname_text = 'Player'
        self.lvl_count = 1
        self.lives_count = 3
        self.highscore_count = 0
        self.nickname = TextObject(self.game, text=self.get_nickname_text(), color=Color.RED, x=0, y=0)
        self.lvl = TextObject(self.game, text=self.get_lvl_text(), color=Color.RED, x=0, y=0)
        self.score = ScoreObject(self.game, color=Color.RED)
        self.lives = LivesObject(self.game, x=15, y=self.game.HEIGHT - 30)
        self.highscore = TextObject(self.game, text=self.get_highscore_text(), color=Color.RED, x=0, y=0)
        self.update_texts()
        self.objects += [self.nickname, self.lvl, self.score, self.lives, self.highscore]
        self.field = FieldObject(self.game, 70, 35, 17, 17)
        self.objects.append(self.field)
        self.objects = self.field.add_seeds(self.objects)
        self.pacman = PacmanObject(self.game, 300, 427)
        self.objects.append(self.pacman)
        self.orange_ghost = OrangeGhostObject(self.game, 272, 273)
        self.objects.append(self.orange_ghost)
        self.red_ghost = RedGhostObject(self.game, 302, 222)
        self.objects.append(self.red_ghost)

    def update_texts(self) -> None:
        self.nickname.update_text(self.get_nickname_text())
        self.nickname.move_center(self.game.WIDTH - self.nickname.rect.width // 2 - 15, 15)
        self.lvl.update_text(self.get_lvl_text())
        self.lvl.move_center(60, 15)
        self.score.move_center(60, 40)
        self.lives.move_center(15, self.game.HEIGHT - 15)
        self.highscore.update_text(self.get_highscore_text())
        self.highscore.move_center(self.game.WIDTH // 2, 15)

    def additional_event_check(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.PAUSE_SCENE_INDEX)

    def on_activate(self) -> None:
        self.update_texts()

    def get_nickname_text(self) -> str:
        return self.nickname_text

    def get_lvl_text(self) -> str:
        return 'lvl{}'.format(self.lvl_count)

    def get_lives_text(self) -> str:
        return str(self.lives_count)

    def get_highscore_text(self) -> str:
        return 'Лучший результат: {}'.format(self.highscore_count)

    def check_score(self) -> None:
        pass

    def check_game_over(self) -> None:
        if not self.lives.get_live_status():
            self.game.set_scene(self.game.GAMEOVER_SCENE_INDEX)

    def additional_logic(self) -> None:
        self.pacman.collect_seed(self.objects, self.score)
        self.pacman.collide_ghosts(self.objects)
        self.check_score()
        self.check_game_over()
