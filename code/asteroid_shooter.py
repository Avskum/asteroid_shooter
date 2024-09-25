import pygame, sys, os
from random import randint, uniform

from pygame import Vector2


def laser_update(laser_list, speed = 400):
    for rect in laser_list:
        rect.y -= round(speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)

def meteor_update(meteor_list, speed = 10):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)


def display_score():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    pygame.draw.rect(display_surface, (255, 0, 0), text_rect.inflate(10,30), 3, 3)
    display_surface.blit(text_surf,text_rect)

def laser_timer(can_shoot, duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

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
meteor_img_path = os.path.join(graphics_folder, 'meteor.png')

font_path = os.path.join(graphics_folder, 'subatomic.ttf')




#import ship
ship_surf = pygame.image.load(ship_image_path).convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

#background
bg_surf = pygame.image.load(bg_image_path).convert_alpha()
bg_rect = bg_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

#laser
laser_surf = pygame.image.load(laser_img_path).convert_alpha()
#laser_rect = laser_surf.get_rect(midbottom = ship_rect.midbottom)
laser_list = []

#meteor rect
meteor_surf = pygame.image.load(meteor_img_path).convert_alpha()
meteor_list = []

#laser timer
can_shoot = True
shoot_time = None

#import text
font = pygame.font.Font(font_path,50)


#meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer,2000)

#game loop
while True:
    display_surface

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:

            #laser
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midbottom)
            laser_list.append(laser_rect)

            #timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer:
            x_pos = randint(-100,WINDOW_WIDTH + 100)
            y_pos = randint(-100,-50)

            #meteor
            meteor_rect = meteor_surf.get_rect(center=(x_pos, -y_pos))

            #create rand dir
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)

            meteor_list.append((meteor_rect,direction))




    #mouse input
    position = pygame.mouse.get_pos()
    ship_rect.center = position
    click_pos = pygame.mouse.get_pressed()

    #framerate limit
    dt = clock.tick(144) / 1000

    #UPDATE
    laser_update(laser_list)
    meteor_update(meteor_list, 300)
    can_shoot = laser_timer(can_shoot, 400)

    #meteor ship collisions
    for meter_tuple in meteor_list:
        meteor_rect = meter_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()


    #laser meteor collisions
    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                meteor_list.remove(meteor_tuple)
                laser_list.remove(laser_rect)
                print('collision')

    #drwaing of surfs
    display_surface.blit(bg_surf,(0,0))

    display_score()


    for rect in laser_list:
        display_surface.blit(laser_surf, rect)

    for meter_tuple in meteor_list:
        display_surface.blit(meteor_surf, meter_tuple[0])

    display_surface.blit(ship_surf, ship_rect)

    #draw final frame
    pygame.display.update()
    #print(len(laser_list))