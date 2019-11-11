class Player:

    def __init__(self):
        self.direction = 0
        self.head_color = (255,0,0)
        self.body_color = (0,255,255)
        self.headx = 20
        self.heady = 20
        self.speed = 5

    def move(self):
        '''Moves snake at certain speed'''
        if self.direction == 0:
            self.headx += self.speed
        elif self.direction == 1:
            self.heady += self.speed
        elif self.direction == 2:
            self.headx -= self.speed
        elif self.direction == 3:
            self.heady -= self.speed

        return self.headx,self.heady

    def add_tail(self):
        '''Adds pixel to the end of the snake after eating an apple''' # maybe part of App class?
        pass

    def end(self):
        '''Checks whether or not the head of the snake hits the body'''
        pass

    def change_direction(self,e):
        '''Changes direction upon keypress
        0 = right
        1 = down
        2 = left
        3 = up
        '''

        if e == 275:
            self.direction = 0
        elif e == 274:
            self.direction = 1
        elif e == 276:
            self.direction = 2
        elif e == 273:
            self.direction = 3

        return self.direction