from pieces import color, King, Queen, Rook, Knight, Bishop, Pawn
from board import Board
import os

class ChessBot:
    def __init__(self, max_depth, on_turn):
        self.board = Board(self, on_turn)
        self.max_depth = max_depth
        self.on_turn = on_turn

    def calculate_next_move(self):
        self.depth = 0
        self.progress = [{"%": 0, "cur": 0, "max": 0} for i in range(self.max_depth)]
        self.generate_boards(self.board)
        self.get_best_move()
        return self.board.next_board.made_move

    def generate_boards(self, board):
        all_moves = board.all_moves()

        # Output
        # os.system('clear')
        print(board.__repr__(highlight=None))
        print(f"Depth: {self.depth}")
        """ print(f"On turn: {board.on_turn}") """

        # all moves
        h = [i[2:] for i in all_moves]

        self.depth += 1
        if self.depth < self.max_depth:
            for move in all_moves:
                new_board = board.copy()
                new_board.move(move)
                board.children.append(new_board)

                self.generate_boards(new_board)

        self.depth -= 1

    def get_best_move(self):
        self.min_max(self.board)

    def min_max(self, board):
        if board.children:
            for child in board.children:
                self.min_max(child)

            board.next_board = sorted(board.children, key=lambda x: x.value, reverse=True if self.on_turn == board.on_turn else False)[0]
            board.value = board.next_board.value
        else:
            board.calc_value(self.on_turn)

if __name__ == "__main__":
    chess_bot = ChessBot(3, color.WHITE)
    chess_bot.board.load(open('board.txt'))
    move = chess_bot.calculate_next_move()
    print(move)

    """print(chess_bot.board.pieces[10])
    moves = chess_bot.board.pieces[10].all_moves()
    print(moves)
    h = [i[2:] for i in moves]
    print(chess_bot.board.__repr__(highlight=h))"""
