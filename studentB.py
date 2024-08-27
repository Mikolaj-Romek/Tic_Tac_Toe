import random


#Ruch użytkownika
def get_user_move(board):
    while True:
        try:
            move = input("Podaj swój ruch jako: 'rząd, kolumna' (0 do 2 dla obu): ").strip()
            row, col = map(int, move.split(','))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                return board
            else:
                print("Ta komórka jest już wypełniona.")
        except (ValueError, IndexError):
            print("Złe dane. Podaj swój ruch jako: 'rząd, kolumna' (0 do 2 dla obu): ")


#Ruch komputera
def ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
    return board


def is_player_starting():
    choice = input("Czy chcesz zacząć? (y/n)? ").strip().lower()
    return choice == 'y'
