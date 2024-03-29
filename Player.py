class Player:

    def __init__(self):
        self.x = [50] # position 0 is head
        self.y = [50] # position 0 is head
        self.head_color =(255,0,0)
        self.body_color = (255,255,0)
        self.steps = 10
        self.speed = 0
        self.length = 0 # number of body parts
        self.direction = None # game starts paused
        self.updateCount = 0
        self.updateCountMax = 2
        self.score = 0
        


    def move(self):
        #update position of body
        self.updateCount += 1

        if self.updateCount > self.updateCountMax:
            if self.length >= 1:
                for i in range(self.length,0,-1):
                    self.x[i] = self.x[i-1]
                    self.y[i] = self.y[i-1]
            

            #update position of head
            if self.direction == 0 : # go right
                self.x[0] += self.steps
            elif self.direction == 1: # go left
                self.x[0] -= self.steps
            elif self.direction == 2: # go up
                self.y[0] -= self.steps
            elif self.direction == 3: # go down
                self.y[0] += self.steps

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
        if self.direction == 0: # right
            self.x.append(self.x[-1] - self.steps)
            self.y.append(self.y[-1])

        elif self.direction == 1: # left
            self.x.append(self.x[-1] + self.steps)
            self.y.append(self.y[-1])

        elif self.direction == 2: # up
            self.y.append(self.y[-1] + self.steps)
            self.x.append(self.x[-1])

        elif self.direction == 3: # down
            self.y.append(self.y[-1] - self.steps)
            self.x.append(self.x[-1])
        
        self.length += 1


    def snakeHeadPos(self):
        return self.x[0],self.y[0]

    def snakeHeadX(self):
        return self.x[0]
    
    def snakeHeadY(self):
        return self.y[0]

    def snakeBodyPos(self):
        return zip(self.x[1:],self.y[1:])
    
    def incScore(self):
        self.score += 1