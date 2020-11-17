import pygame

from scenes import BaseScene
from objects import GhostBase


class MainScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.ghost = GhostBase(game)

    def process_logic(self):
        self.ghost.process_logic()

    def process_draw(self):
        self.ghost.process_draw()
