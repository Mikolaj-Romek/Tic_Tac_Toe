# main.py
from studentA import print_board, new_board, is_game_over
from studentB import ai_move, get_user_move, is_player_starting
from announce_outcome import announce_outcome


def main():
    board = new_board()
    players_move = is_player_starting()

    while not is_game_over(board):
        print_board(board)
        if players_move:
            board = get_user_move(board)
        else:
            board = ai_move(board)

        players_move = not players_move

    print_board(board)
    announce_outcome(board)


if __name__ == '__main__':
    main()
