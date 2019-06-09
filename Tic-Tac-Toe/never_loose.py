def lost(table):
    for i in range(1,4):
        if (table[3*(i-1)]=='O' and table[3*(i-1)+1]=='O' and table[3*(i-1)+2]=='O' ) or (table[i-1]=='O' and table[ i+2]=='O' and table[i+5]=='O'): 
            return True
    if (table[0]=='O' and table[4]=='O' and table[8]=='O') or (table[2]=='O' and table[4]=='O' and table[6]=='O'):
        return True
    return False

def won(table):
    for i in range(1,4):
        if (table[3*(i-1)]=='X' and table[3*(i-1)+1]=='X' and table[3*(i-1)+2]=='X' ) or (table[i-1]=='X' and table[ i+2]=='X' and table[i+5]=='X'): 
            return True
    if (table[0]=='X' and table[4]=='X' and table[8]=='X') or (table[2]=='X' and table[4]=='X' and table[6]=='X'):
        return True
    return False


def predict(table, co):
    if co == 0:
        if lost(table): 
            return -1
        elif won(table):
            return +1
    return 0


            
def divide(table, co):      #Problem somewhere here
    l={}
    for c,i in enumerate(table):
        if i=='':
            l[c]=0

    for i in l.keys():

        tab_predict=table

        if co % 2 == 0:
            tab_predict[i]='X'
        else:
            tab_predict[i]='O'
        if predict(tab_predict, co-1)<1:
            l[i]-=predict(tab_predict, co-1)

    best = table
    if co % 2 == 0:
        best[min(l, key=l.get)] = 'X'
    else:
        best[min(l, key=l.get)] = 'O'
    
    return best


def show(table):
    for c, i in enumerate(table):
        if i=='':
            print("[",c+1,"]", end = '')
        else:
            print("[",i,"]", end = '')
        if c%3==2:
            print()
    return

free_cells = 9
table = [ '' ] * 9
print("Let's play!\n")

while '' in table:
    show(table)
    try:
        i=int(input("Number of field to make move: "))
        table[ i-1 ] = 'O'
        free_cells -= 1
    except:
        continue
    show(table)
    print()
 
    x=divide(table,free_cells)
    free_cells -= 1
    if x!=0:
        print(x)
        table=x
    else: 
        print("Impossibru")
        break
