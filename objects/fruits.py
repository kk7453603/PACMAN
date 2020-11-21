import pygame
import random

class Cherry(object):
    def __init__(self, pac_man_x, pac_man_y, lives, seeds, points) -> None:
        self.pac_man_x = pac_man_x
        self.pac_man_y = pac_man_y
        self.lives = lives
        self.seeds = seeds
        self.points = points

    def Cherry(self, points, pac_man_x, pac_man_y, lives ):
        cherry = pygame.image.load('cherry.png')
        kol = 0
        if (points == 70):
            y = random.randint(0,800)
            x = random.randint(0,1000)
            screen.blit(cherry, (x, y))
            if (pac_man_y == y and pac_man_x == x):
                kol += 1
                if (kol == 4):
                    lives += 1




