import time


#Sprawdzenie kto wygrał
def check_win(char, board):
    # Sprawdź wiersze
    for row in board:
        if row.count(char) == 3:
            return True
    # Sprawdź kolumny
    for col in range(3):
        if all(board[row][col] == char for row in range(3)):
            return True
    # Sprawdź przekątne
    if all(board[i][i] == char for i in range(3)):
        return True
    if all(board[i][2 - i] == char for i in range(3)):
        return True
    return False


def announce_outcome(board):
    if check_win('X', board):
        print("Wygrałeś!")
        time.sleep(3)
    elif check_win('O', board):
        print("Przegrałeś z botem")
        time.sleep(3)
    else:
        print("Remis")
        time.sleep(3)
