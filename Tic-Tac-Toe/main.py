import never_loose

free_cells = 9
tab = [ '' ] * 9
sign=''
while sign!='O' and sign!='X':
    sign = input("Co wybierasz? O/X  ").upper()


print("Let's play!\n")

if sign == 'X':
    tab[ randint( 0, 8 ) ] = 'O'
    comp_sign = 'O'
    free_cells -= 1
else:
    comp_sign = 'X'

while free_cells > 0 :
    show(tab)

    i=int(input("Number of field to make move: "))
    while tab[i-1]!='':
        print("Wrong number")
        i=int(input("Number of field to make move: "))
    tab[ i-1 ] = sign
    free_cells -= 1

    show(tab)
    print()
    
    if free_cells>0:
        tab=move(tab, free_cells, comp_sign)
        free_cells -= 1

    if won(tab, comp_sign):
        show(tab)
        print("You lost!")
        break

    if free_cells == 0:
        show(tab)
        print("Draw!")
    