import pygame
from App import App
from Player import Player
import time


App = App()
clock = pygame.time.Clock()
running = True

App.draw_game()
while running:
    clock.tick(40)
    for event in pygame.event.get():
        #closes game
        if event.type == pygame.QUIT:
            running = False
        
        #change direction on key press
        if event.type == pygame.KEYDOWN: 
            if event.key == 273:
                #App.player.add_body()
                App.player.change_direction(273)
            elif event.key == 274:
                #App.player.add_body()
                App.player.change_direction(274)
            elif event.key == 275:
                #App.player.add_body()
                App.player.change_direction(275)
            elif event.key == 276:
                #App.player.add_body()
                App.player.change_direction(276)
                
        
        #if snake head eats apple



        #if snake head hits body
    App.refresh()
    App.player.move()
    pygame.display.flip()
    time.sleep(50/1000)