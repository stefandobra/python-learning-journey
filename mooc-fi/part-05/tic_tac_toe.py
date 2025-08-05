def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in range(0, 3) or y not in range(0, 3):
        return False
    
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    
    return False


