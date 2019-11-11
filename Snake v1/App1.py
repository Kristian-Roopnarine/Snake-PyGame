import pygame
from Player import Player

class App:

    def __init__(self):
        self.width = 600
        self.height = 600
        self.player = Player()
        self.blocks = 10
        self.background = (0,0,0)
        pygame.init()
    
    def draw_snakehead(self):
        head = pygame.Rect(self.player.body[0][0], self.player.body[0][1], self.blocks, self.blocks)
        pygame.draw.rect(self.screen, self.player.head_color, head)
    
    def draw_body(self):
        self.player.add_body()
        for body in self.player.body:
            x,y = body
            body = pygame.Rect(x,y,self.blocks,self.blocks)
            pygame.draw.rect(self.screen,self.player.body_color,body)
    
    def draw_snake(self):
        self.draw_snakehead()
        self.draw_body()
        
    def draw_apple(self):
        pass

    def draw_game(self):
        self.screen = pygame.display.set_mode((self.width,self.height))
        for y in range(self.height//10):
            for x in range(self.width//10):
                rect = pygame.Rect(y * self.blocks, x * self.blocks,self.blocks,self.blocks)
                pygame.draw.rect(self.screen,self.background,rect)
        

    def refresh(self):
        self.screen.fill(self.background)
        self.draw_snake()
        #self.draw_snakehead()
        #self.draw_body()


    def detect_keypress(self,e):
        if e.type == pygame.KEYDOWN:
            if e.key == 273:
                pass
            elif e.key == 274:
                pass
            elif e.key == 275:
                pass
            elif e.key == 276:
                return 276
