import random

class Apple:

    def __init__(self):
        self.color = (0,128,0)
        self.eaten = False
        self.position = [random.randint(0,59) * 10,random.randint(0,59) * 10]

    
    def getX(self):
        return self.position[0]
    
    def getY(self):
        return self.position[1]
    
    def pos(self):
        return self.position[0],self.position[1]

    def newApple(self):
        self.position = [random.randint(0,59) * 10,random.randint(0,59) * 10]
