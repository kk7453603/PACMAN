from .image import ImageObject

class SeedObject:
    
    def __init__(self, game, type):
        super().__init__(game)
        self.type = type
        if type = 0:
            filename = 'point.png'
        else:
            filename = 'tablet.png'
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

    def draw_seed(self):
        screen.blit(self.image, self.rect)
