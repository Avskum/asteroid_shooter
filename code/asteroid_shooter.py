import pygame, sys, os

pygame.init()

##folders & paths
game_folder = os.path.dirname(os.path.dirname(__file__))

graphics_folder = os.path.join(game_folder, 'graphics')
ship_image_path = os.path.join(graphics_folder, 'ship.png')
bg_image_path = os.path.join(graphics_folder, 'background.png')

font_path = os.path.join(graphics_folder, 'subatomic.ttf')

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
window_name = pygame.display.set_caption("Meteor Shooter")
clock = pygame.time.Clock()


#import img
ship_surf = pygame.image.load(ship_image_path).convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
print(ship_rect)
shipy_y_pos = 500

bg_surf = pygame.image.load(bg_image_path).convert_alpha()

#import text
font = pygame.font.Font(font_path,50)
text_surf = font.render('Asteroid Shooter', True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))


#keep code working
while True:
    display_surface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            ship_rect.center = event.pos

    #framerate limit
    clock.tick(144)

    display_surface.blit(bg_surf,(0,0))

    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,text_rect)

    pygame.display.update()