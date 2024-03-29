import pygame
from Player import Player
from Apple import Apple
import time
import random
from tkinter import *
from tkinter import messagebox

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
        self.clock = pygame.time.Clock()
        self.apple = Apple()
        self.active = False
        Tk().wm_withdraw()
    
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
        self.drawApple()
        pygame.display.set_caption('Snake Game. Your Score is: %s' % (self.player.score))
        pygame.display.update()

    def drawApple(self):
        apple = pygame.Rect(self.apple.getX(),self.apple.getY(),self.block,self.block)
        pygame.draw.rect(self.screen,self.apple.color,apple)
    
    def startOver(self):
        self.player.score = 0
        self.player.length = 0
        self.player.direction = None
        self.player.x = [50]
        self.player.y = [50]
        self.player.speed = 0
        self.active = False

    def endApp(self):
        self.running = False
        
    def startApp(self):
        self.drawGame()
        self.drawSnake()
        self.drawApple()
        pygame.display.flip()
        self.player.speed = 0

        while self.running:
            if self.active:
                self.clock.tick(40 + (self.player.speed * 5))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.endApp()

                    if event.type == pygame.KEYDOWN:
                        self.player.change_direction(event.key)
                        
                
                # if snake eats apple
                if self.player.snakeHeadPos() == self.apple.pos():

                    # add snake body
                    self.player.add_body()

                    # generate new apple
                    self.apple.newApple()

                    #increase score and speed
                    self.player.incScore()
                    self.player.speed += 1

                # if snake hits itself
                if self.player.snakeHeadPos() in self.player.snakeBodyPos():
                    if messagebox.askyesnocancel('Game over.','You ran into yourself! Do you want to start over?') == True:
                        self.startOver()
                    else:
                        self.endApp()
                    

                #if snake hits edge of window
                if self.player.snakeHeadY() < 0 or self.player.snakeHeadY() == 600 or self.player.snakeHeadX() < 0 or self.player.snakeHeadX() == 600:
                    if messagebox.askyesnocancel('Game over.','You ran into yourself! Do you want to start over?') == True:
                        self.startOver()
                    else:
                        self.endApp()
                
                
                self.player.move()
                self.updateGame()

            else:
                #waits for key input
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.endApp()

                    if event.type == pygame.KEYDOWN:
                        self.player.change_direction(event.key)
                        self.active = True


        


    
