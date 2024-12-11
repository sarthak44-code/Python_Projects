import pygame

# pygame setup
pygame.init()
gray = (119,118,110)
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

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
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
        car(x,y)
        if x>680-car_width or x <110:
            bumped = True
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

