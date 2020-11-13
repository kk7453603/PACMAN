from .image import ImageObject

class Seed:
    
    def __init__(self, type):
        self.type = type
        if type = 0:
            self.image = pygame.image.load('point.png')
        else:
            self.image = pygame.image.load('tablet.png')
        self.rect = self.image.get_rect()

    def draw_seed(selfб x, y):
        screen.blit(self.image, self.rect)
