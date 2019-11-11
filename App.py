import pygame
from Player import Player
import time

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
        snake_size = len(self.player.x)

        for j in range(snake_size):
            for i in range(snake_size):
                if i == 0 and j == 0: # if snake head
                    rect = pygame.Rect(self.player.x[i],self.player.y[j],self.block,self.block)
                    pygame.draw.rect(self.screen,self.player.head_color,rect)
                    print('Head drawn')
                else: # if body
                    rect = pygame.Rect(self.player.x[i],self.player.y[j],self.block,self.block)
                    pygame.draw.rect(self.screen,self.player.body_color,rect)
                    print('Body drawn')

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
            
            self.player.move()
            time.sleep(100/1000)

        


    def endApp(self):
        self.running = False
