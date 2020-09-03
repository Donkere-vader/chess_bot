from pieces import color, King, Queen, Rook, Knight, Bishop, Pawn

class Board:
    empty_board = [[None for i in range(8)] for i in range(8)]

    def __init__(self, game):
        self.game = game
        self.board = self.empty_board

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

        _board = self.empty_board

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

            piece = pieces[piece_char](self.game, self.get_let(piece_x), piece_y, piece_color)

            _board[piece_y][piece_x] = piece
            x += 2

        self.board = _board

    def get_x(self, char):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(char.lower())

    def get_let(self, x):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][x]

    def tile(self, x, y, piece=None):
        xnum = self.get_x(x)

        if piece is None:
            return self.board[y][xnum]
        else:
            self.baord[y][xnum] = piece

    def __repr__(self):
        output = ""

        for y in range(8):
            for x in range(8):
                piece = self.board[y][x]
                if piece is None:
                    output += "|  "
                    continue
                output += f"|{piece.color.upper()[:1]}{piece.char.upper()}"
            output += "|\n"

        return output

if __name__ == "__main__":
    board = Board(None)
    board.load(open('board.txt'))
    print(board)
