import pandas as pd
from random import randint

class Player:

    def __init__(self):
        self.table=['A','B','C','D','E','F','G','H','I','J']
        self.field=pd.DataFrame([['  .' for j in "ABCDEFGHIJ"]for i in range(1,11)], columns=self.table, index=[str(i) for i in range(1,11)])
        self.enemy_view=pd.DataFrame([[' ? ' for j in "ABCDEFGHIJ"]for i in range(1,11)], columns=self.table, index=[str(i) for i in range(1,11)])
        self.ships=[4,3,2,1]
        self.hp=20
        self.dd=['H','V']

    def place(self, size, coordinates, direction='V', show=False):
        try:
            size=int(size)
        except:
            print("Wrong size format! Select numper between 1-4")
            return
        if  size<1 or size>4 or self.ships[size-1]==0:
            print("You don't have ship of this size.")
            return 

        x, y = coordinates.upper().split()

        if (x not in ['A','B','C','D','E','F','G','H','I','J']) or (y not in '12345678910'):
            print("Wrong coordinates! Correct format: A 1")
            return

        x_num=self.table.index(x)

        if not( direction.upper().startswith('H') or direction.upper().startswith('V')):
            print("Wrong direction! Correct format: H for horizontal or V for vertical")
            return

        if direction.upper().startswith('V'):
            for i in range(size):
                if int(y)+i>10 or '.' not in self.field[x][str(int(y)+i)]:
                    if show == True: 
                        print("You can't put your's ship here")
                    return

            for i in range(size):
                self.field[x][str(int(y)+i)]="\u2588\u2588\u2588"

                if x_num>1:
                    self.field[self.table[x_num-1]][str(int(y)+i)]= '   '
                if x_num<9:
                    self.field[self.table[x_num+1]][str(int(y)+i)]= '   '

            if int(y)+size<11:
                if x_num>1:
                    self.field[self.table[x_num-1]][str(int(y)+size)]= '   '
                self.field[self.table[x_num]][str(int(y)+size)]= '   '
                if x_num<9:
                    self.field[self.table[x_num+1]][str(int(y)+size)]= '   '
        
            if int(y)-1>0:     
                if x_num>1:
                    self.field[self.table[x_num-1]][str(int(y)-1)]= '   '
                self.field[self.table[x_num]][str(int(y)-1)]= '   '
                if x_num<9:
                    self.field[self.table[x_num+1]][str(int(y)-1)]= '   '
        
        else:
            for i in range(size):
                if x_num+i>9 or '.' not in self.field[self.table[x_num+i]][y]:
                    print("You can't put your's ship here")
                    return
                 
            for i in range(size):
                self.field[self.table[x_num+i]][y]="\u2588\u2588\u2588"

                if int(y)>1:
                    self.field[self.table[x_num+i]][str(int(y)-1)]= '   '
                if int(y)<10:
                    self.field[self.table[x_num+i]][str(int(y)+1)]= '   '

            if x_num+size<10:
                if int(y)>1:
                    self.field[self.table[x_num+size]][str(int(y)-1)]= '   '
                self.field[self.table[x_num+size]][y]= '   '
                if x_num<9:
                    self.field[self.table[x_num+size]][str(int(y)+1)]= '   '
        
            if x_num>0:     
                if x_num>1:
                    self.field[self.table[x_num-1]][str(int(y)-1)]= '   '
                self.field[self.table[x_num-1]][y]= '   '
                if x_num<9:
                    self.field[self.table[x_num-1]][str(int(y)+1)]= '   '

        self.ships[size-1]-=1

    def attacked(self, coordinates):
        try:
            x, y = coordinates.upper().split()
        except:
            print("try again")
            return False

        if (x not in ['A','B','C','D','E','F','G','H','I','J']) or (y not in '12345678910'):
            print("Wrong coordinates! Correct format: A 1")
            return False

        if '?' not in self.enemy_view[x][y]:
            print("You attacked this place before!")
            print(self.enemy_view)
            return False

        if self.field[x][y] == '\u2588\u2588\u2588':
            self.field[x][y] = '\u2588X\u2588'
            self.enemy_view[x][y] = ' X '
            print("Hit! Attack again!")
            self.hp -= 1
            return False

        else:
            self.enemy_view[x][y] = '   '
            print("Missed!")
            return True

def game2players():
    player_1=Player()
    player_2=Player()

    print("Player one! Place your's ships!")
    for c, i in enumerate(player_1.ships):
        while player_1.ships[c]>0:
            print(player_1.field)
            print("You have",player_1.ships[c],"ships of size",c+1,"remaining")
            coord=input("Coordinates of ship's head (ex. 'A 1'): ")
            dire=input("Direction(h/v): ")
            if dire=='':
                player_1.place(c+1, coord, 'V', True)
            else:
                player_1.place(c+1, coord, dire)

    print("Player two! Place your's ships!")
    for c, i in enumerate(player_2.ships):
        while player_2.ships[c]>0:
            print(player_2.field)
            print("You have",player_2.ships[c],"ships of size",c+1,"remaining")
            coord=input("Coordinates of ship's head (ex. 'A 1'): ")
            dire=input("Direction(h/v): ")
            if dire=='':
                player_2.place(c+1, coord, 'V', True)
            else:
                player_2.place(c+1, coord, dire)

    while player_1.hp>0 and player_2.hp>0:

        print("Player 1 turn!")
        while True:
            print(player_2.enemy_view)
            coord = input("Attack coordinates: ")
            if player_2.attacked(coord):
                break


        print("Player 2 turn!")
        while True:
            print(player_1.enemy_view)
            coord = input("Attack coordinates: ")
            if player_1.attacked(coord):
                break

    if player_1.hp>0:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

def game1player():
    player=Player()
    computer=Player()

    print("Player! Place your's ships!")
    for c, i in enumerate(player.ships):
        while player.ships[c]>0:
            print(player.field)
            print("You have",player.ships[c],"ships of size",c+1,"remaining")
            coord=input("Coordinates of ship's head (ex. 'A 1'): ")
            dire=input("Direction(h/v): ")
            if dire=='':
                player.place(c+1, coord, 'V', True)
            else:
                player.place(c+1, coord, dire)

    for c, i in enumerate(computer.ships):
        while computer.ships[c]>0:
            y = str(randint(1,10))
            x = computer.table[randint(0,9)]
            dire=computer.dd[randint(0,1)]
            computer.place(c+1, x +' '+ y, dire)

    while player.hp>0 and computer.hp>0:

        print("Player's turn!")
        while True:
            print(computer.enemy_view)
            coord = input("Attack coordinates: ")
            if computer.attacked(coord):
                break


        print("Computer's turn!")
        while True:
            print(player.field)
            y = str(randint(1,10))
            x = computer.table[randint(0,9)]
            if player.attacked(x+y):
                break

    if player.hp>0:
        print("Player wins")
    else:
        print("Computer wins")

def quick_game():
    player=Player()
    computer=Player()

    for c, i in enumerate(player.ships):
        while player.ships[c]>0:
            y = str(randint(1,10))
            x = player.table[randint(0,9)]
            dire=player.dd[randint(0,1)]
            player.place(c+1, x +' '+ y, dire)

    for c, i in enumerate(computer.ships):
        while computer.ships[c]>0:
            y = str(randint(1,10))
            x = computer.table[randint(0,9)]
            dire=computer.dd[randint(0,1)]
            computer.place(c+1, x +' '+ y, dire)

    while player.hp>0 and computer.hp>0:

        print("Player's turn!")
        while True:
            print(player.field)
            print(computer.enemy_view)
            coord = input("Attack coordinates: ")
            if computer.attacked(coord):
                break


        print("Computer's turn!")
        while True:
            y = str(randint(1,10))
            x = computer.table[randint(0,9)]
            if player.attacked(x+' '+y):
                break

    if player.hp>0:
        print("Player wins")
    else:
        print("Computer wins")


quick_game()