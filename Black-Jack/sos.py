def begin():
    print("Welcome in Casino de Royal\n\nIt seems that you have no money, so take this 100$ and have some fun!\nAre you familiar with Black Jack rules?\n\nWe are playing with one deck of cards.\nTo win you need to achive higer score than The Dealer, but not greater then 21.\nIn case of draw, nobody wins.")
    print("To win you need to achive higer score than The Dealer, but not greater then 21.\nIn case of draw, nobody wins.")
    colours =  {0:'clubs', 1:'diamonds', 2:'hearts', 3:'spades'}
    values = {1:'Ace', 2:'Two ', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Jack', 11:'Queen', 12:'King'}
    while True:
        no = input("No of players")
    return 

class player:
    def __init__(self, b=True):
        self.cards = []
        self.sum = 0
        self.ace = False
        self.money=100
    
    def get_card(self):
        from random import randint as rand
        self.col = colours[rand(0,3)]
        self.val = rand(1,12)
        self.sum += self.val
        if self.val == 1:
            self.ace = True 
        self.cards.append(values[self.val]+' of '+self.col)

    def bid(self, x):
        while x > self.money:
            x = input("Too much!\nBid: ")
        self.bid = x
        self.money -= x

    def move(self, action):
        print("You have",self.sum,"points:")
        for i in self.cards:
            print('\t'+i)
        m=input("h to hit, s to stand or d to double")




class croupier:
    def __init__(self):
        self.cards = []
        self.sum = 0
        self.ace = False
        self.bot = b
    
    def get_card():
        from random import randint as rand
        self.col = colours[rand(0,3)]
        self.val = rand(1,12)
        self.sum += self.val
        if self.val == 1:
            self.ace = True 
        self.cards.append(values[self.val]+' of '+self.col)

    def show():
        for i in self.cards:
            print(i)