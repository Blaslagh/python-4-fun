import random

class Creature:

    def __init__(self,x,y):
        self.energy = 100
        self.direction = random.randint(1,4)
        self.distance = random.randint(1,10)
        self.x = x
        self.y = y
        return
    
    def reproduce(self):
        if self.energy >= 200 :
            self.energy -= 100
            return True
        return False

    def feed(self, amount):
        self.energy+=amount
        return

    def move(self):
        if self.distance>0:
            if self.direction = 1 and 

