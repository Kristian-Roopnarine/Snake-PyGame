import random

class Apple:

    def __init__(self):
        self.color = (0,128,0)
        self.eaten = False
        self.position = [random.randint(30,450),random.randint(30,450)]

    
    def getX(self):
        return self.position[0]
    
    def getY(self):
        return self.position[0]

    def newApple(self):
        self.position = [random.randint(30,450),random.randint(30,450)]
