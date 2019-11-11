import time
class Player:

    def __init__(self):
        self.direction = 0
        self.head_color = (255,0,0)
        self.body_color = (0,255,255)
        self.speed = 5
        #self.body = [[self.headx,self.heady]]
        self.body = [[30,30]] # self.body[0] = head

    def move(self):
        '''Moves snake at certain speed'''

        # updates position of snake head
        if self.direction == 0:
            self.body[0][0] += self.speed
        elif self.direction == 1:
            self.body[0][1] += self.speed
        elif self.direction == 2:
            self.body[0][0] -= self.speed
        elif self.direction == 3:
            self.body[0][1] -= self.speed 
        print(self.body)

        body_length = len(self.body)
        #update positions of body
        '''
        if body_length > 1:
            for i in range(body_length-1,0,-1):
                self.body[i] = self.body[i-2]
        '''
        
    def add_body(self):
        '''Adds pixel to the end of the snake after eating an apple''' # maybe part of App class?
        '''We need to add one whole rectangle BEHIND the head'''
        '''self.body will contain a list of ALL body coordinates and head coordinates'''
        tail = self.body[-1]
        if self.direction == 0:
            body = [tail[0]-15, tail[1]]
            self.body.append(body)
        elif self.direction == 1:
            body = [tail[0],tail[1] - 15]
            self.body.append(body)
        elif self.direction == 2:
            body =[tail[0] + 15,tail[1]]
            self.body.append(body)
        elif self.direction == 3:
            body = [tail[0],tail[1] + 15]
            self.body.append(body)

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