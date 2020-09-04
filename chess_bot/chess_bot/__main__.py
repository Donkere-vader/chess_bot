from pieces import color, King, Queen, Rook, Knight, Bishop, Pawn
from board import Board


class ChessBot:
    def __init__(self, max_depth, on_turn):
        self.board = Board(self)
        self.max_depth = max_depth
        self.on_turn = on_turn

    def calculate_next_move(self):
        pass

    def best_move(self):
        all_moves = self.board.get_all_moves(self.on_turn)

if __name__ == "__main__":
    chess_bot = ChessBot(5, color.WHITE)
    chess_bot.board.load(open('board.txt'))
    print(chess_bot.board.pieces[16])
    moves = chess_bot.board.pieces[16].all_moves()
    print(moves)
    print(chess_bot.board.__repr__(highlight=moves))
