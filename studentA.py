import turtle
from announce_outcome import check_win

# Ustawienia ekranu
screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.setup(width=600, height=600)

# Konfiguracja żółwia
drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()


#Rysowanie planszy
def draw_board():
    drawer.penup()
    drawer.goto(-300, 100)
    drawer.pendown()
    drawer.forward(600)
    drawer.penup()
    drawer.goto(-300, -100)
    drawer.pendown()
    drawer.forward(600)

    drawer.penup()
    drawer.goto(-100, 300)
    drawer.setheading(-90)
    drawer.pendown()
    drawer.forward(600)
    drawer.penup()
    drawer.goto(100, 300)
    drawer.pendown()
    drawer.forward(600)


#Rysowanie odpowiednich symboli
def draw_symbol(row, col, symbol):
    x = col * 200 - 300 + 100
    y = -row * 200 + 300 - 150
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.write(symbol, align="center", font=("Arial", 80, "normal"))


#Wyświetlanie planszy
def print_board(board):
    drawer.clear()
    draw_board()
    for i in range(3):
        for j in range(3):
            if board[i][j] != ' ':
                draw_symbol(i, j, board[i][j])


#Tworzenie pustej planszy
def new_board(size=3):
    return [[' ' for _ in range(size)] for _ in range(size)]


def is_game_over(board):
    return check_win('X', board) or check_win('O', board) or all(
        board[i][j] != ' ' for i in range(len(board)) for j in range(len(board)))
