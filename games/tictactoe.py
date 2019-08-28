from random import randint

def show(table):
    for c, i in enumerate(table):
        if i=='':
            print("[",c+1,"]", end = '')
        else:
            print("[",i,"]", end = '')
        if c%3==2:
            print()
    return

def won(table, sign):   #works fine
    for i in range(1,4):
        if (table[3*(i-1)]==sign and table[3*(i-1)+1]==sign and table[3*(i-1)+2]==sign ) or (table[i-1]==sign and table[ i+2]==sign and table[i+5]==sign): 
            return True
    if (table[0]==sign and table[4]==sign and table[8]==sign) or (table[2]==sign and table[4]==sign and table[6]==sign):
        return True
    return False
            
def move(table, free_cells, comp_sign, sign): #This function gives you a chance of winning :)
    if table[4]=='':
        return 4
    if free_cells % 2 == 1:
        temp_sign = 'X'
    else:
        temp_sign = 'O'


    for c, i in enumerate(table):
        if i != '':
            continue
        if free_cells==1:
            return c
        
        temp_tab=table[:]
        temp_tab[c]=temp_sign
        if temp_sign=='X':
            temp_tab[move(temp_tab, free_cells-1, comp_sign, sign)]='O'
        else:
            temp_tab[move(temp_tab, free_cells-1, comp_sign, sign)]='X'
        if won(temp_tab, sign):
            return c
    while True:
        c=randint(0,8)
        if table[c]=='':
            break
    return c
    
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def start():
    free_cells = 9
    sign=''
    while sign!='O' and sign!='X':
        sign = input("You would like to be? O/X ").upper()
    print("Let's play!\n")
    return sign

def game(sign, free_cells=9):
    tab = [ '' ] * 9
    if sign == 'X':
        tab[ randint( 0, 8 ) ] = 'O'
        comp_sign = 'O'
        free_cells -= 1
    else:
        comp_sign = 'X'


    while free_cells > 0 :
        show(tab)
        print()

        i=int(input("Number of field to make move: "))
        while tab[i-1]!='' and free_cells > 0 :
            print("Wrong number")
            i=int(input("Number of field to make move: "))
        tab[ i-1 ] = sign
        free_cells -= 1
        if won(tab, sign):
            show(tab)
            print("You won!")
            break
        if free_cells>0:
            x=move(tab, free_cells, comp_sign, sign)
            tab[x]=comp_sign
            free_cells -= 1

        if won(tab, comp_sign):
            show(tab)
            print("You lost!")
            break

        if free_cells == 0:
            show(tab)
            return "Draw!"
    return 0

def play():
    while True:
        game(start())
        if not playAgain():
            break
    return 0