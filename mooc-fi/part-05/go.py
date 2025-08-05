def who_won(game_board: list):
    one = 0
    two = 0

    for row in game_board:
        for element in row:
            if element == 1:
                one += 1
            elif element == 2:
                two += 1
    
    if one > two:
        return 1
    elif one == two:
        return 0
    else:
        return 2
    
    
