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
        self.running = True
    
    def drawSnake(self):
        # get positions of snake and turn into rectangles
        for y in self.player.y:
            for x in self.player.x:
                if x == 0: # if snake head
                    rect = pygame.Rect(x,y,self.block,self.block)
                    pygame.draw.rect(self.screen,self.player.head_color,rect)
                else: # if body
                    rect = pygame.Rect(x,y,self.block,self.block)
                    pygame.draw.rect(self.screen,self.player.body_color,rect)

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
        self.drawGame()
        self.drawSnake()
        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endApp()
                
        


    def endApp(self):
        self.running = False
