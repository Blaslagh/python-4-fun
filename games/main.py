while True:
    game = input("Pick a game:\n1-tic tac toe\n2-blackjack\n3-battleships\nq-quit\n\n")
    try:
        print("\n\n\n\n\n")
        game = int(game)
        if game==1:
            import tictactoe
            tictactoe.play()
        elif game==2:
            import blackjack
            blackjack.play()
        elif game==3:
            import battleships
            battleships.play()
    except:
        if game.upper()=='Q': break