class Player:

    def __init__(self):
        self.x = [50,40,30,20] # position 0 is head
        self.y = [50,50,50,50] # position 0 is head
        self.head_color =(255,0,0)
        self.body_color = (255,255,0)
        self.speed = 5
        self.length = 3 # no body parts yet
        self.direction = 0


    def move(self):

        #update position of head
        if self.direction == 0 : # go right
            self.x[0] += self.speed
        elif self.direction == 1: # go left
            self.x[0] -= self.speed
        elif self.direction == 2: # go up
            self.y[0] -= self.speed
        elif self.direction == 3: # go down
            self.y[0] += self.speed
        
            #update position of body


    def change_direction(self,e):
        if e == 273:
            self.direction = 2
        elif e == 274:
            self.direction = 3
        elif e == 275:
            self.direction = 0
        elif e == 276:
            self.direction = 1

    def add_body(self):
        pass
