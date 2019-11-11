import pygame
from Player import Player

class App:

    def __init__(self):
        self.width = 600
        self.height = 600
        self.player = Player()
        self.block = 10
        self.background = (0,0,0)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
    
    def drawSnake(self):
        pass

    def drawGame(self):
        for y in range(self.height//10):
            for x in range(self.width//10):
                rect = pygame.Rect(x * self.block ,y* self.block ,self.block,self.block)
                pygame.draw.rect(self.screen,self.background,rect)

    def updateGame(self):
        pass

    def drawApple(self):
        pass

    def startApp(self):
        pass

    def endApp(self):
        pass
