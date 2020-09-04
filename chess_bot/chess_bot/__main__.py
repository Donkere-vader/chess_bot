from pieces import color, King, Queen, Rook, Knight, Bishop, Pawn
from board import Board


class ChessBot:
    def __init__(self, max_depth, on_turn):
        self.board = Board(self)
        self.max_depth = max_depth

    def calculate_next_move(self):
        self.generate_boards(self.board)

    def generate_boards(self, board):
        all_moves = board.all_moves()
        print(all_moves)

if __name__ == "__main__":
    chess_bot = ChessBot(5, color.WHITE)
    chess_bot.board.load(open('board.txt'))
    # chess_bot.calculate_next_move()

    print(chess_bot.board.pieces[10])
    moves = chess_bot.board.pieces[10].all_moves()
    print(moves)
    h = [i[2:] for i in moves]
    print(chess_bot.board.__repr__(highlight=h))
    chess_bot.board.move(moves[1])
    print(chess_bot.board)
