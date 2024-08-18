import pygame, sys, os

# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
window_name = pygame.display.set_caption("Meteor Shooter")
clock = pygame.time.Clock()

##folders & paths
game_folder = os.path.dirname(os.path.dirname(__file__))

graphics_folder = os.path.join(game_folder, 'graphics')
ship_image_path = os.path.join(graphics_folder, 'ship.png')
bg_image_path = os.path.join(graphics_folder, 'background.png')
laser_img_path = os.path.join(graphics_folder, 'laser.png')

font_path = os.path.join(graphics_folder, 'subatomic.ttf')




#import ship
ship_surf = pygame.image.load(ship_image_path).convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

#background
bg_surf = pygame.image.load(bg_image_path).convert_alpha()

#laser
laser_surf = pygame.image.load(laser_img_path).convert_alpha()
#laser_rect = laser_surf.get_rect(midbottom = ship_rect.midbottom)
laser_list = []

#import text
font = pygame.font.Font(font_path,50)
text_surf = font.render('Asteroid Shooter', True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))


#game loop
while True:
    display_surface

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print('shoot laser')
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midbottom)
            laser_list.append(laser_rect)
            print(laser_list)

    #mouse input
    position = pygame.mouse.get_pos()
    ship_rect.center = position
    click_pos = pygame.mouse.get_pressed()

    #framerate limit
    dt = clock.tick(144) / 1000

    #laser go up
    #laser_rect.y -= round(400 * dt)




    #drwaing of surfs
    display_surface.blit(bg_surf,(0,0))
    pygame.draw.rect(display_surface, (255, 0, 0), text_rect.inflate(10,30), 3, 3)
    display_surface.blit(text_surf,text_rect)

    for laser in laser_list:
        display_surface.blit(laser_surf, laser)
        laser.y -= round(700 * dt)


    display_surface.blit(ship_surf, ship_rect)


    #draw final frame
    pygame.display.update()