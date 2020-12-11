from datetime import datetime
import  pygame
from constants import Color
from objects import TextObject
from scenes import BaseScene


class FinalScene(BaseScene):
    TEXT_FMT = 'Game over ({})'
    seconds_to_end = 4
    def __init__(self, game) -> None:
        self.last_seconds_passed = 0
        super().__init__(game)
        self.update_start_time()
        self.a = pacman()
        self.b = ghost()
        self.c = fiar_ghost()
        self.time_current = datetime.now()
        self.seconds_passed = (self.time_current - self.time_start).seconds

    def on_activate(self) -> None:
        self.update_start_time()

    def update_start_time(self) -> None:
        self.time_start = datetime.now()

    def get_gameover_text_formatted(self) -> str:
        return self.TEXT_FMT.format(self.seconds_to_end - self.last_seconds_passed)

    def create_objects(self) -> None:

        self.text = TextObject(
            self.game,
            text=self.get_gameover_text_formatted(), color=Color.RED,
            x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2
        )
        self.objects.append(self.text)

    def additional_logic(self) -> None:
        time_current = datetime.now()
        seconds_passed = (time_current - self.time_start).seconds
        if self.last_seconds_passed != seconds_passed:
            self.last_seconds_passed = seconds_passed
            self.objects[0].update_text(self.get_gameover_text_formatted())
        if seconds_passed >= self.seconds_to_end:
            self.game.set_scene(self.game.MENU_SCENE_INDEX)
    def process_draw(self) -> None:
        self.screen.fill((17, 14, 61))
        self.a.process_draw(self.screen)
        self.b.process_draw(self.screen)
        self.c.process_draw(self.screen)
        font = pygame.font.Font('images/Final/Shift.ttf', 50)
        text = font.render("GAME OVER", False, (255, 255, 255))
        self.screen.blit(text, (75, 225))
    def process_logic(self) -> None:
        self.a.process_logic()
        self.b.process_logic()
        self.c.process_logic()
        self.additional_logic()
    def process_event(self, event: pygame.event.Event) -> None:
        pass

    def on_deactivate(self) -> None:
        pass

    def on_window_resize(self) -> None:
        self.text.move_center(x=self.game.WIDTH // 2, y=self.game.HEIGHT // 2)

class pacman:
    sprites = [pygame.image.load('images/Final/pacman/1.png'),
               pygame.image.load('images/Final/pacman/2.png'),
               pygame.image.load('images/Final/pacman/3.png'),
               pygame.image.load('images/Final/pacman/4.png'),
               pygame.image.load('images/Final/pacman/5.png'),
               pygame.image.load('images/Final/pacman/6.png'),
               pygame.image.load('images/Final/pacman/7.png'),
               pygame.image.load('images/Final/pacman/8.png'),
               pygame.image.load('images/Final/pacman/9.png'),
               pygame.image.load('images/Final/pacman/10.png'),
               pygame.image.load('images/Final/pacman/11.png'),
               ]

    def __init__(self):
        self.tick  = 0
        self.img_index = 0

    def process_logic(self):
        self.tick += 4
        if (self.tick % 10 == 0):
            self.img_index += 1
            self.img_index %= 9

    def process_draw(self, screen):
        screen.blit(pygame.transform.scale(pacman.sprites[self.img_index], (125,125)), (85, 320))

class ghost:
    sprites = [pygame.image.load('images/Final/gohst/1.png'),
               pygame.image.load('images/Final/gohst/2.png'),
               pygame.image.load('images/Final/gohst/3.png'),
               pygame.image.load('images/Final/gohst/4.png'),
               pygame.image.load('images/Final/gohst/5.png'),
               pygame.image.load('images/Final/gohst/1.png'),
               pygame.image.load('images/Final/gohst/2.png'),
               pygame.image.load('images/Final/gohst/3.png'),
               pygame.image.load('images/Final/gohst/4.png')
               ]

    def __init__(self):
        self.tick  = 0
        self.img_index = 0

    def process_logic(self):
        self.tick += 5
        if (self.tick % 10 == 0):
            self.img_index += 1
            self.img_index %= 9

    def process_draw(self, screen):
        screen.blit(pygame.transform.scale(ghost.sprites[self.img_index], (120,120)), (400, 320))


class fiar_ghost:
    sprites = [pygame.image.load('images/Final/fiar_gohst/1.png'),
               pygame.image.load('images/Final/fiar_gohst/2.png'),
               pygame.image.load('images/Final/fiar_gohst/3.png'),
               pygame.image.load('images/Final/fiar_gohst/4.png'),
               pygame.image.load('images/Final/fiar_gohst/3.png'),
               pygame.image.load('images/Final/fiar_gohst/2.png'),
               pygame.image.load('images/Final/fiar_gohst/1.png'),
               pygame.image.load('images/Final/fiar_gohst/1.png'),
               pygame.image.load('images/Final/fiar_gohst/2.png'),
               pygame.image.load('images/Final/fiar_gohst/3.png'),
               ]

    def __init__(self):
        self.tick  = 0
        self.img_index = 0

    def process_logic(self):
        self.tick += 5
        if (self.tick % 10 == 0):
            self.img_index += 1
            self.img_index %= 10

    def process_draw(self, screen):
        screen.blit(pygame.transform.scale(fiar_ghost.sprites[self.img_index], (120,120)), (240, 320))
