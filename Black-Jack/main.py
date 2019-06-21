def begin():
    print("Welcome in Casino de Royal\n\nYou start with 100$\nAre you familiar with Black Jack rules?\n\nWe are playing with one deck of cards.\nTo win you need to achive higer score than The Dealer,\n but not greater then 21.\nIn case of draw, nobody wins.")
    

class player:
    def __init__(self):
        self.cards = []
        self.sum = 0
        self.ace = False
        self.money=100
    
    def get_card(self):
        colours =  {0:'clubs', 1:'diamonds', 2:'hearts', 3:'spades'}
        values = {1:'Ace', 2:'Two ', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:"Ten", 11:'Jack', 12:'Queen', 13:'King'}

        from random import randint as rand
        col = colours[rand(0,3)]
        val = rand(1,12)
        self.sum += val
        if val == 1:
            self.ace = True 
            self.sum += 10
        if self.sum>21:
            if self.ace:
                self.sum-=10
        self.cards.append(values[val]+' of '+col)

    def bet(self):
        print("Money:",self.money)
        x = int(input("Bid: "))
        while x > self.money:
            x = int(input("Too much!\nBid: "))
        self.bid = x
        self.money -= x

    def move(self):
        print("You have",self.sum,"points:")
        for i in self.cards:
            print('\t'+i)
        while True:
            m=input("h to hit, s to stand, q to quit").lower()
            if m in ['h','s','q']:
                return m


class croupier:
    def __init__(self):
        self.cards = []
        self.sum = 0
        self.ace = 0
    
    def get_card(self):
        colours =  {0:'clubs', 1:'diamonds', 2:'hearts', 3:'spades'}
        values = {1:'Ace', 2:'Two ', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:"Ten", 11:'Jack', 12:'Queen', 13:'King'}

        from random import randint as rand
        col = colours[rand(0,3)]
        val = rand(1,12)
        self.sum += val
        if val == 1: 
            self.ace += 1 
            self.sum += 10
        if self.sum>21:
            if self.ace>0:
                self.sum -= 10
                self.ace -= 1
        self.cards.append(values[val]+' of '+col)
        if len(self.cards)>1:
            print("Croupier got: "+values[val]+' of '+col)
        else:
            print("Croupier got hidden card")
        return 0

    def show(self):
        print("Croupier has",self.sum)
        for i in self.cards:
            print(i)


def play():
    begin()
    input("Press Enter to continue")
    Cro = croupier()
    pl = player()
    move='h'
    while move!='q':
        move='h'
        pl.cards=[]
        Cro.cards=[]
        pl.sum=0
        Cro.sum=0
        pl.bet()
        pl.get_card()
        Cro.get_card()
        pl.get_card()
        Cro.get_card()
        while pl.sum<21 and len(pl.cards)<5 and move=='h':
            move=pl.move()
            if move == 'q':
                break
            if move == 'h':
                pl.get_card()
        if move == 'q':
            break
        if pl.sum == 21:
            print("Blackjack! You win!")
            pl.money += 2 * pl.bid
            continue
        if pl.sum>21:
            print("Too much! You lost!")
        else:
            Cro.show()
            while (Cro.sum<pl.sum or Cro.sum<17) and len(Cro.cards)<5:
                Cro.get_card()
            if Cro.sum>21:
                print("Dealer busted!")
                pl.money += 2 * pl.bid
            elif pl.sum==Cro.sum:
                print("\nYour points:",pl.sum,"\nCroupier points:",Cro.sum)
                print("Draw")
                pl.money +=  pl.bid
            elif pl.sum>Cro.sum:
                print("\nYour points:",pl.sum,"\nCroupier points:",Cro.sum)
                print("You win!")
                pl.money += 2 * pl.bid
            else:
                print("\nYour points:",pl.sum,"\nCroupier points:",Cro.sum)
                print("You lost!")
        if pl.money==0:
            print("You lost all money! \n\nTake this 100$ if you want to play again.")
            pl.money = 100