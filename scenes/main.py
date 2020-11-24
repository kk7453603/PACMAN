from random import randint
from typing import Tuple

import pygame

from constants import Color
from objects import FieldObject
from objects import GhostBase
from objects import PacmanObject
from objects import TextObject, ScoreObject, LivesObject
from scenes import BaseScene


class MainScene(BaseScene):
    MAX_COLLISIONS = 15
    BALLS_COUNT = 3

    def create_objects(self) -> None:
        self.start_time = pygame.time.get_ticks()
        self.exit_time = self.start_time + 1000
        self.nickname_text = 'Player'
        self.lvl_count = 1
        self.highscore_count = 0
        self.nickname = TextObject(self.game, text=self.get_nickname_text(), color=Color.RED, x=0, y=0)
        self.lvl = TextObject(self.game, text=self.get_lvl_text(), color=Color.RED, x=0, y=0)
        self.score = ScoreObject(self.game, color=Color.RED)
        self.lives = LivesObject(self.game, x=15, y=self.game.HEIGHT - 30)
        self.highscore = TextObject(self.game, text=self.get_highscore_text(), color=Color.RED, x=0, y=0)
        self.ghost = GhostBase(self.game, 345, 300)
        self.field = FieldObject(self.game, 150, 105)
        self.pacman = PacmanObject(self.game, 150, 105)
        self.update_texts()
        self.objects += [self.nickname, self.lvl, self.score, self.lives, self.highscore, self.field, self.ghost,
                         self.pacman]

    def update_texts(self) -> None:
        self.nickname.update_text(self.get_nickname_text())
        self.nickname.move_center(self.game.WIDTH - self.nickname.rect.width // 2 - 15, 15)
        self.lvl.update_text(self.get_lvl_text())
        self.lvl.move_center(60, 15)
        self.score.move_center(60, 40)
        self.lives.move_center(15, self.game.HEIGHT - 15)
        self.highscore.update_text(self.get_highscore_text())
        self.highscore.move_center(self.game.WIDTH // 2, 15)

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.PAUSE_SCENE_INDEX)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ghost.pressed = 'left'
                if event.key == pygame.K_RIGHT:
                    self.ghost.pressed = 'right'
                if event.key == pygame.K_UP:
                    self.ghost.pressed = 'up'
                if event.key == pygame.K_DOWN:
                    self.ghost.pressed = 'down'
                if event.key == pygame.K_a:
                    self.pacman.pressed = 'left'
                if event.key == pygame.K_d:
                    self.pacman.pressed = 'right'
                if event.key == pygame.K_w:
                    self.pacman.pressed = 'up'
                if event.key == pygame.K_s:
                    self.pacman.pressed = 'down'
            elif event.type == pygame.KEYUP:
                self.ghost.pressed = 'none'

    def get_random_position(self, radius: int) -> Tuple[int, int]:
        return randint(10, self.game.WIDTH - radius * 2 - 10), randint(10, self.game.HEIGHT - radius * 2 - 10)

    def on_activate(self) -> None:
        self.update_texts()

    def pacman_ghost_collision(self, pacman, ghost):
        if pacman.rect.colliderect(ghost.rect):
            if ghost.status == 'scared':
                self.score.ghost_eaten()
                self.ghost.moving_home = True

    def get_nickname_text(self) -> str:
        return self.nickname_text

    def get_lvl_text(self) -> str:
        return 'lvl{}'.format(self.lvl_count)

    def get_lives_text(self) -> str:
        return str(self.lives_count)

    def get_highscore_text(self) -> str:
        return 'Лучший результат: {}'.format(self.highscore_count)

    """
    def check_score(self) -> None:
        if self.score.get_score() >= (self.lives.get_max_lives_count() - self.lives.get_lives_count() + 1) * 100:
            self.lives.reduce_lives()
    """

    def check_game_over(self) -> None:
        if not self.lives.get_live_status():
            self.game.set_scene(self.game.GAMEOVER_SCENE_INDEX)

    def additional_logic(self) -> None:
        self.pacman_ghost_collision(self.pacman, self.ghost)
    #    self.check_score()
        self.check_game_over()
