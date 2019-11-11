import pygame
from Player import Player

class App:

    def __init__(self):
        self.width = 600
        self.height = 600
        self.player = Player()
        pygame.init()
    
    def draw_snake(self):
        pass
    
    def draw_body(self):
        pass
    
    def draw_apple(self):
        pass

    def draw_game(self):
        self.screen = pygame.display.set_mode((self.width,self.height))

    def detect_keypress(self):
        pass
