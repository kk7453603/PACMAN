import pygame


class DrawableObject:     # TODO: bring here pygame.sprite.Sprite inheritance
    def __init__(self, game) -> None:
        self.game = game
        self.rect = pygame.rect.Rect(0, 0, 0, 0)

    def move(self, x: int, y: int) -> None:
        self.rect.x = x
        self.rect.y = y

    def move_center(self, x: int, y: int) -> None:
        self.rect.centerx = x
        self.rect.centery = y

    def process_event(self, event: pygame.event.Event) -> None:
        pass

    def process_logic(self) -> None:
        pass

    def process_draw(self) -> None:
        pass  # use self.game.screen for drawing, padawan
