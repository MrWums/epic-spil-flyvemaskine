import pygame
from player import player_class
from map import map_class
from knap import knap_class


#-------------------game setup stuff---------------------------
pygame.init()
screenwidth, screenheight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()

plane_sprite = pygame.transform.scale_by(pygame.image.load("images/plane.png"),0.5)
tower_sprite = pygame.image.load("images/tower.png")
ground_sprite = pygame.image.load("images/ground.png")
tutorial = pygame.transform.scale_by(pygame.image.load("images/tutorial.png"),0.68)

#----------------------Menu stuff------------------------------
font = pygame.font.SysFont("Arial", 30)
textcolor = (0, 0, 0)

start_knap = knap_class(screenwidth/2, screenheight*0.25, 100, 100, "Start", font, textcolor)
tutorial_knap = knap_class(screenwidth/2, screenheight*0.5, 100, 100, "How to play", font, textcolor)
quit_knap = knap_class(screenwidth/2, screenheight*0.75, 100, 100, "Quit", font, textcolor)
back_knap = knap_class(screenwidth/4, screenheight*0.5, 100, 100, "Back", font, textcolor)

gamestate = "menu"

while True:
    events = pygame.event.get()
    if gamestate == "menu":
        display.fill((6,97,170))
        start_knap.draw(display)
        tutorial_knap.draw(display)
        quit_knap.draw(display)

        for event in events:
            if start_knap.klik(event):
                gamestate = "game"
                player = player_class(display, plane_sprite, screenheight)
                map = map_class(display, tower_sprite, ground_sprite, (0, screenheight - 100),(2500, screenheight - 668))

            if tutorial_knap.klik(event):
                gamestate = "tutorial"

            if quit_knap.klik(event):
                exit()


    if gamestate == "tutorial":
        display.fill((6, 97, 170))
        display.blit(tutorial,(0,0))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamestate = "menu"


    if gamestate == "game":
        clock.tick(60)
        display.fill((6,97,170))

        player_pos = player.update(events)
        map_pos = map.update()

        # Det her er kinda scuffed og jeg forstår det kun halvt selv haha. Player_pos kan både return en vector med den position eller "quit"
        if player_pos == "quit":
            gamestate = "menu"
        else:
            if map_pos.x+151 >= player_pos.x >= map_pos.x:
                if player_pos.y > map_pos.y:
                    points = int((player_pos.y-map_pos.y)//5)
                    gamestate = "win_screen"

        for i in range(10):
            map.draw(i)

    if gamestate == "win_screen":
        display.fill((6, 97, 170))
        text1 = font.render(f"You got {points}/100 points!",True,(0,0,0),(6,97,170))
        text2 = font.render("Press ESC to return to menu",True,(0,0,0),(6,97,170))

        text1Rect = text1.get_rect()
        text1Rect.center = (screenwidth/2,screenheight/2)
        text2Rect = text2.get_rect()
        text2Rect.center = (screenwidth/2,(screenheight/2)+100)

        display.blit(text1,text1Rect)
        display.blit(text2,text2Rect)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamestate = "menu"

    pygame.display.flip()