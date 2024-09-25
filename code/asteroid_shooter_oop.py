import pygame, sys

class Ship(pygame.sprite.Sprite):
    def __init__(self,groups):
        #init parent class
        super().__init__(groups)
        #surface img
        self.image = pygame.image.load('../graphics/ship.png').convert_alpha()
        #rect img
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def update(self):
        self.input_position()
class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/laser.png')
        self.rect = self.image.get_rect(midbottom = pos)

#basic setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
window_name = pygame.display.set_caption("Meteor Shooter")
clock = pygame.time.Clock()


#background
backgroud_surf = pygame.image.load('../graphics/background.png').convert()

#sprite groups
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

#sprite creation
ship = Ship(spaceship_group)

laser = Laser((100,300),laser_group)

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    dt = clock.tick() / 1000

    #background
    display_surface.blit(backgroud_surf,(0,0))


    #update
    spaceship_group.update()


    #graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    pygame.display.update()