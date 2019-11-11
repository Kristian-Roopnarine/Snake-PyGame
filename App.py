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
        self.snake = []
        self.clock = pygame.time.Clock()
    
    def drawSnake(self):
        # get positions of snake and turn into rectangles
        snake_size = len(self.player.x)

        for i in range(snake_size):
            
            if i == 0: # if snake head
                head = pygame.Rect(self.player.x[i],self.player.y[i],self.block,self.block)
                pygame.draw.rect(self.screen,self.player.head_color,head)
                

            else: # if body
                rect = pygame.Rect(self.player.x[i],self.player.y[i],self.block,self.block)
                pygame.draw.rect(self.screen,self.player.body_color,rect)
                    

    def drawGame(self):
        for y in range(self.height//10):
            for x in range(self.width//10):
                rect = pygame.Rect(x * self.block ,y* self.block ,self.block,self.block)
                pygame.draw.rect(self.screen,self.background,rect)

    def updateGame(self):
        self.screen.fill(self.background)
        self.drawSnake()
        pygame.display.update()

    def drawApple(self):
        pass

    def startApp(self):
        self.drawGame()
        pygame.display.flip()

        while self.running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endApp()

                if event.type == pygame.KEYDOWN:
                    self.player.change_direction(event.key)
            
            self.player.move()
            self.updateGame()
            

        


    def endApp(self):
        self.running = False
