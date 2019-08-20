import random

class Creature:

    def __init__(self, size, x, y):
        self.energy = 100
        self.direction = random.randint(1,4)
        self.distance = 0
        self.size = size*(1+random.randint(-5,5)/100)

class Enviorment:
    def __init__(self, size, dif):
        self.field = [['E']*size]*size
        