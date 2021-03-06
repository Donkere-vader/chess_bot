from pieces import color, King, Queen, Rook, Knight, Bishop, Pawn
from copy import deepcopy

class Board:
    empty_board = [[None for i in range(8)] for i in range(8)]

    def __init__(self, game, on_turn):
        self.game = game
        self.board = deepcopy(self.empty_board)
        self.on_turn = on_turn
        self.children = []
        self.value = None

    def copy(self):
        new_board = Board(self.game, self.on_turn)

        new_board.board = deepcopy(self.empty_board)
        for piece in self.pieces:
            new_piece = piece.__class__(new_board, piece.x, piece.y, piece.color)
            new_board.board[new_piece.y][self.get_x(new_piece.x)] = new_piece

        return new_board

    def calc_value(self, color) -> int:
        total_own_points = 0
        total_other_points = 0
        for piece in self.pieces:
            possible_moves = len(piece.all_moves())
            total_piece_value = possible_moves * piece.value
            if color == color:
                total_own_points += total_piece_value
            else:
                total_other_points += total_piece_value

        self.value = total_own_points - total_other_points

    @property
    def pieces(self) -> list:
        pieces = []
        for y in self.board:
            for x in y:
                if x is not None:
                    pieces.append(x)

        return pieces

    def load(self, file):
        self.loads(file.read())

    def loads(self, board_str):
        board_lst = list(board_str.replace('\n', ''))

        _board = deepcopy(self.empty_board)

        pieces = {
            "k": King,
            "q": Queen,
            "b": Bishop,
            "h": Knight,
            "r": Rook,
            "p": Pawn
        }

        x = 0
        while x < 8 * 8 * 2:
            piece_y = int((x / 2) / 8)
            piece_x = int((x / 2) - (piece_y * 8))

            piece_color = color.BLACK if board_lst[x].lower() == 'b' else color.WHITE
            piece_char = board_lst[x + 1].lower()

            if piece_char not in pieces:
                x += 2
                continue

            piece = pieces[piece_char](self, self.get_let(piece_x), piece_y, piece_color)

            _board[piece_y][piece_x] = piece
            x += 2

        self.board = _board

    def get_x(self, char):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(char.lower())

    def get_let(self, x):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][x]

    def tile(self, x, y, piece=None):
        if type(x) == str:
            xnum = self.get_x(x)
        else:
            xnum = x

        if piece is None:
            return self.board[y][xnum]
        else:
            self.baord[y][xnum] = piece

    def move(self, move: str):
        frm = move[:2]
        to = move[2:]

        frm_x = self.get_x(frm[0])
        frm_y = int(frm[1])
        to_x = self.get_x(to[0])
        to_y = int(to[1])

        piece = self.tile(frm_x, frm_y)

        self.board[to_y][to_x] = piece
        self.board[frm_y][frm_x] = None
        piece.x = self.get_let(to_x)
        piece.y = to_y

        self.on_turn = color.BLACK if self.on_turn == color.WHITE else color.WHITE
        self.made_move = move

    def all_moves(self):
        moves = []

        for piece in self.pieces:
            if piece.color != self.on_turn:
                continue

            moves += piece.all_moves()

        return moves

    def str_pos(self, x, y):
        if type(x) != str:
            x = self.get_let(x)

        return f"{x}{y}"

    def tile_exists(self, x, y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False

    def __repr__(self, highlight=None):
        output = ""

        for y in reversed(range(8)):
            for x in range(8):
                piece = self.board[y][x]
                if piece is None:
                    new = "  "
                else:
                    new = f"{piece.color.upper()[:1]}{piece.char.upper()}"

                if highlight is not None and self.str_pos(x, y) in highlight:
                    new = f"\033[30;42m{new}\033[0;0m"

                output += "|" + new
            output += "|\n"

        return output

if __name__ == "__main__":
    board = Board(None)
    board.load(open('board.txt'))
    print(board.__repr__())
