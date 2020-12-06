import pygame

from constants import Color
from objects import ButtonObject
from scenes import BaseScene


class Icon(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.set_color(self.image, Color.WHITE)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def set_color(self, img, color):
        for x in range(img.get_width()):
            for y in range(img.get_height()):
                color.a = img.get_at((x, y)).a  # Preserve the alpha value.
                img.set_at((x, y), color)  # Set the color of the pixel.


class Settings(BaseScene):
    def create_objects(self) -> None:
        self.sound_icon = Icon('images/menu/sound.png', [380, 138])
        self.button_sound = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 - 175, 200, 50,
            Color.BLACK, self.sound_change, "ВЫКЛЮЧИТЬ ЗВУК"
        )

        self.button_back = ButtonObject(
            self.game,
            self.game.WIDTH // 2 - 100, self.game.HEIGHT - 50 - 25, 200, 50,
            Color.BLACK, self.back_to_menu, 'НАЗАД'
        )
        self.objects = [self.button_sound, self.button_back]

    def sound_change(self):
        if self.button_sound.text == "ВЫКЛЮЧИТЬ ЗВУК":
            self.button_sound.set_text("ВКЛЮЧИТЬ ЗВУК")
            self.sound_icon = Icon('images/menu/no-sound.png', [380, 138])
        else:
            self.button_sound.set_text("ВЫКЛЮЧИТЬ ЗВУК")
            self.sound_icon = Icon('images/menu/sound.png', [380, 138])

    def back_to_menu(self) -> None:
        self.game.set_scene(self.game.MENU_SCENE_INDEX)

    def on_window_resize(self) -> None:
        self.button_back.move(self.game.WIDTH // 2 - 100, self.game.HEIGHT - 50 - 25)

    def additional_draw(self) -> None:
        self.screen.blit(self.sound_icon.image, self.sound_icon.rect)
