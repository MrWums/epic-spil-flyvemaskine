import pygame
from player import player_class
from map import map_class
from important_stuff import knap_class, text, explosion_class


#-------------------game setup stuff---------------------------
pygame.init()
pygame.mixer.init()

screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwidth,screenheight))
base_w,base_h = 1920,1080
scale_x = screenwidth/base_w
scale_y = screenheight/base_h
scale_factor = min(scale_x,scale_y)

clock = pygame.time.Clock()

plane_sprite = pygame.transform.scale_by(pygame.image.load("assets/plane.png"),0.5*scale_factor)
tower_sprite = pygame.transform.scale_by(pygame.image.load("assets/tower.png"),scale_factor)
ground_sprite = pygame.transform.scale_by(pygame.image.load("assets/ground.png"),scale_factor)
tutorial = pygame.transform.scale(pygame.image.load("assets/tutorial.png"),(screenwidth,screenheight))

map_length = 100

# Don't know wtf this is but it works
explosion_group = pygame.sprite.Group()

#----------------------Menu stuff------------------------------
font = pygame.font.SysFont("Arial", 30)
textcolor = (0, 0, 0)

# Knapper
start_knap = knap_class(screenwidth/2, screenheight*0.25, 100, 100, "Start", font, textcolor)
tutorial_knap = knap_class(screenwidth/2, screenheight*0.5, 100, 100, "How to play", font, textcolor)
quit_knap = knap_class(screenwidth/2, screenheight*0.75, 100, 100, "Quit", font, textcolor)
back_knap = knap_class(screenwidth/4, screenheight*0.5, 100, 100, "Back", font, textcolor)

# Farver
dark_red = (105,0,17)
sky_blue = (6,97,170)
black = (0,0,0)
white = (255,255,255)

gamestate = "menu"

while True:
    clock.tick(60)
    events = pygame.event.get()
    explosion_group.draw(display)
    explosion_group.update()


    if gamestate == "menu":
        display.fill(sky_blue)
        start_knap.draw(display)
        tutorial_knap.draw(display)
        quit_knap.draw(display)

        for event in events:
            if start_knap.klik(event):
                gamestate = "game"
                player = player_class(display, plane_sprite, screenheight,scale_factor)
                map = map_class(display, tower_sprite, ground_sprite, (0, screenheight - 100*scale_factor),(2500*scale_factor, screenheight - 668*scale_factor),scale_factor)

            if tutorial_knap.klik(event):
                gamestate = "tutorial"

            if quit_knap.klik(event):
                exit()


    if gamestate == "tutorial":
        display.fill(sky_blue)
        display.blit(tutorial,(0,0))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamestate = "menu"


    if gamestate == "game":
        display.fill(sky_blue)

        player_pos = player.update(events)
        map_pos = map.update(player.started)

        # Det her er kinda scuffed og jeg forstår det kun halvt selv haha. Player_pos kan både return en vector med den position eller "quit"
        if player_pos == "quit":
            gamestate = "menu"
        elif player_pos == "dead":
            gamestate = "dead"
        else:
            if map_pos.x+151 >= player_pos.x >= map_pos.x or map_pos.x+151 >= player_pos.x-700 >= map_pos.x:
                if player_pos.y > map_pos.y:
                    points = int((player_pos.y-map_pos.y)//5)
                    gamestate = "win_screen"
                    exp_played = False

        # Tegn ground texture tingen x antal gange efter hinanden
        for i in range(map_length):
            map.draw(i,player.started)

        # Text der siger press W to start
        if player.started == False:
            text(display,screenwidth/2,screenheight/2,"Press W to start",font,white,sky_blue)


    if gamestate == "win_screen":

        if exp_played == False:
            win_timer = pygame.time.get_ticks()
            explosion = explosion_class(player.x+250, player.y+30,scale_factor)
            explosion_group.add(explosion)
            exp_played = True

        if pygame.time.get_ticks() - win_timer > 2000:

            display.fill(sky_blue)

            text(display,screenwidth/2,screenheight/2-50,f"Congratulations! You hit the target and got {points}/100 points!",font,white,sky_blue)
            text(display, screenwidth/2,screenheight/2+50,"Press ESC to return to menu", font, white, sky_blue)

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gamestate = "menu"


    if gamestate == "dead":
        display.fill(black)
        text(display, screenwidth/2,screenheight/2-50, "Wrong target, don't aim for Pentagon", font, dark_red, black)
        text(display,screenwidth/2,(screenheight/2)+50,"Press ESC to return to menu",font,dark_red,black)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamestate = "menu"

    pygame.display.flip()