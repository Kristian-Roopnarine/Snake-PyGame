class Player:

    def __init__(self):
        self.x = [50,40,30,20] # position 0 is head
        self.y = [50,50,50,50] # position 0 is head
        self.head_color =(255,0,0)
        self.body_color = (255,255,0)
        self.speed = 10
        self.length = 3 # number of body parts
        self.direction = 0
        self.updateCount = 0
        self.updateCountMax = 5


    def move(self):
        #update position of body
        self.updateCount += 1

        if self.updateCount > self.updateCountMax:
            for i in range(self.length,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            

            #update position of head
            if self.direction == 0 : # go right
                self.x[0] += self.speed
            elif self.direction == 1: # go left
                self.x[0] -= self.speed
            elif self.direction == 2: # go up
                self.y[0] -= self.speed
            elif self.direction == 3: # go down
                self.y[0] += self.speed

            self.updateCount = 0

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


    def snakeHeadPos(self):
        return self.x[0],self.y[0]