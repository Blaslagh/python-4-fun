def won(table, sign):
    for i in range(1,4):
        if (table[3*(i-1)]==sign and table[3*(i-1)+1]==sign and table[3*(i-1)+2]==sign ) or (table[i-1]==sign and table[ i+2]==sign and table[i+5]==sign): 
            return True
    if (table[0]==sign and table[4]==sign and table[8]==sign) or (table[2]==sign and table[4]==sign and table[6]==sign):
        return True
    return False


def predict(table, co, sign):
    if co == 0:
        if won(table, sign):
            return 1
    return 0


            
def divide(table, co):      #Problem somewhere here
    #I need to write that function once again


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
