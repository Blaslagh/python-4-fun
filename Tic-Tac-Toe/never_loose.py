from random import randint

def won(table, sign):
    for i in range(1,4):
        if (table[3*(i-1)]==sign and table[3*(i-1)+1]==sign and table[3*(i-1)+2]==sign ) or (table[i-1]==sign and table[ i+2]==sign and table[i+5]==sign): 
            return True
    if (table[0]==sign and table[4]==sign and table[8]==sign) or (table[2]==sign and table[4]==sign and table[6]==sign):
        return True
    return False


            
def move(table, free_cells, comp_sign):
    #Aaaaaaaaaa


def show(table):
    for c, i in enumerate(table):
        if i=='':
            print("[",c+1,"]", end = '')
        else:
            print("[",i,"]", end = '')
        if c%3==2:
            print()
    return
