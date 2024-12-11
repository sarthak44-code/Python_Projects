import pygame
import time
import random


# pygame setup
pygame.init()
gray = (119,118,110)
black = (0,0,0)
display_width = 800
display_height = 600
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()
carimg = pygame.image.load('car1.jpg')
backgroundpic = pygame.image.load('download12.jpg')
yellow_strip = pygame.image.load('yellow strip.jpg')
strip = pygame.image.load('strip.jpg')
car_width = 56

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic = pygame.image.load("car.jpg")
    elif obs==1:
        obs_pic = pygame.image.load("car1.jpg")
    elif obs==2:
        obs_pic = pygame.image.load("car2.jpg")
    elif obs==3:
        obs_pic = pygame.image.load("car4.jpg")
    elif obs==4:
        obs_pic = pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic = pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic = pygame.image.load("car7.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))
    
    


def text_objects(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect = text_objects(text, largetext)
    textrect.center = ((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("YOU CRASHED")

def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))

    gamedisplays.blit(yellow_strip,(375,0))
    gamedisplays.blit(yellow_strip,(375,100))
    gamedisplays.blit(yellow_strip,(375,200))
    gamedisplays.blit(yellow_strip,(375,300))
    gamedisplays.blit(yellow_strip,(375,400))
    gamedisplays.blit(yellow_strip,(375,500))

    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))

def car(x,y):
    gamedisplays.blit(carimg,(x,y))

def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.8)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,(display_width-200))
    obs_starty = -750
    obs_width = 56
    obs_height = 125

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change

        gamedisplays.fill(gray)
        background()
        obs_starty -= (obs_startx/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+= obstacle_speed
        car(x,y)
        if x>680-car_width or x <110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

