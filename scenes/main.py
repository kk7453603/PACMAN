from random import randint
from typing import Tuple

import pygame

from constants import Color
from objects import BallObject, TextObject, ScoreObject
from scenes import BaseScene


class MainScene(BaseScene):
    MAX_COLLISIONS = 15
    BALLS_COUNT = 3

    def create_objects(self) -> None:
        self.balls = [BallObject(self.game) for _ in range(MainScene.BALLS_COUNT)]
        self.nickname_text = 'Player'
        self.lvl_count = 1
        self.lives_count = 3
        self.highscore_count = 0
        self.nickname = TextObject(self.game, text=self.get_nickname_text(), color=Color.RED, x=0, y=0)
        self.lvl = TextObject(self.game, text=self.get_lvl_text(), color=Color.RED, x=0, y=0)
        self.score = ScoreObject(self.game, color=Color.RED)
        self.lives = TextObject(self.game, text=self.get_lives_text(), color=Color.RED, x=0, y=0)
        self.highscore = TextObject(self.game, text=self.get_highscore_text(), color=Color.RED, x=0, y=0)
        self.update_texts()
        self.objects += self.balls
        self.objects += [self.nickname, self.lvl, self.score, self.lives, self.highscore]
        self.reset_balls_position()
        self.set_random_unique_position()

    def update_texts(self) -> None:
        self.nickname.update_text(self.get_nickname_text())
        self.nickname.move_center(self.game.WIDTH - self.nickname.rect.width//2 - 15, 15)
        self.lvl.update_text(self.get_lvl_text())
        self.lvl.move_center(60, 15)
        self.score.move_center(60, 40)
        self.lives.update_text(self.get_lives_text())
        self.lives.move_center(15, self.game.HEIGHT - 15)
        self.highscore.update_text(self.get_highscore_text())
        self.highscore.move_center(self.game.WIDTH//2, 15)

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.PAUSE_SCENE_INDEX)

    def get_random_position(self, radius: int) -> Tuple[int, int]:
        return randint(10, self.game.WIDTH - radius * 2 - 10), randint(10, self.game.HEIGHT - radius * 2 - 10)

    def set_random_position(self, ball: BallObject) -> None:
        pos = self.get_random_position(ball.radius)
        ball.move(*pos)

    def reset_balls_position(self) -> None:
        for ball in self.balls:
            ball.move(self.game.WIDTH, self.game.HEIGHT)

    def set_random_unique_position(self) -> None:
        for index in range(len(self.balls)):
            other_rects = [self.balls[i].rect for i in range(len(self.balls)) if i != index]
            self.set_random_position(self.balls[index])
            while self.balls[index].rect.collidelist(other_rects) != -1:
                self.set_random_position(self.balls[index])

    def on_activate(self) -> None:
        self.collision_count = 0
        self.reset_balls_position()
        self.set_random_unique_position()
        self.update_texts()

    def check_ball_intercollisions(self) -> None:
        for i in range(len(self.balls) - 1):
            for j in range(i + 1, len(self.balls)):
                if self.balls[i].collides_with(self.balls[j]):
                    self.balls[i].bounce(self.balls[j])

    def get_nickname_text(self) -> str:
        return self.nickname_text

    def get_lvl_text(self) -> str:
        return 'lvl{}'.format(self.lvl_count)

    def get_lives_text(self) -> str:
        return str(self.lives_count)

    def get_highscore_text(self) -> str:
        return 'Лучший результат: {}'.format(self.highscore_count)

    def check_ball_edge_collision(self) -> None:
        for ball in self.balls:
            if ball.edge_collision():
                self.score.seed_eaten()

    def check_game_over(self) -> None:
        if self.collision_count >= MainScene.MAX_COLLISIONS:
            self.game.set_scene(self.game.GAMEOVER_SCENE_INDEX)

    def additional_logic(self) -> None:
        self.check_ball_intercollisions()
        self.check_ball_edge_collision()
        self.check_game_over()
