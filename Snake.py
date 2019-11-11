import pygame
from App import App
from Player import Player


App = App()
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    App.player.move()
    App.draw_game()
    App.draw_snake()
    pygame.display.flip()