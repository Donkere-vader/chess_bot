from pieces import color, King, Queen, Rook, Knight, Bishop, Pawn
from board import Board


class ChessBot:
    def __init__(self, max_depth, on_turn):
        self.board = Board(self)
        self.max_depth = max_depth
        self.on_turn = on_turn

    def calculate_next_move(self):
        pass

    def get_best_move(self, on_turn):
        pass

if __name__ == "__main__":
    chess_bot = ChessBot(5, color.WHITE)
    chess_bot.board.load(open('board.txt'))
