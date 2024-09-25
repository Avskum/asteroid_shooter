import pygame, sys

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        #init parent class
        super().__init__()
        #surface img
        self.image = pygame.image.load('../graphics/background.png').convert_alpha()
        #rect img
        self.rect = self.image_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

#basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
window_name = pygame.display.set_caption("Meteor Shooter")
clock = pygame.time.Clock()

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    dt = clock.tick() / 1000

    pygame.display.update()