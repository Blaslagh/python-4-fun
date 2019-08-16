import random

class Creature:

    def __init__(self, x, y):
        self.energy = 100
        self.direction = random.randint(1,4)
        self.distance = random.randint(1,10)

class Field:

    def __init__(self, size, dif):
        self.part = [[food(dif) for j in range(size)] for i in range(size)]
    
    def food(self, dif):
        if random.randint(1,100) <= dif: return 100 + random.randint(-dif,dif)
        else: return "  "