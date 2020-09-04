
class color:
    BLACK = 'black'
    WHITE = 'white'

class Piece:
    def __init__(self, board, x, y, color) -> None:
        self.board = board  # parent board
        self.x = x
        self.y = y
        self.color = color

    def all_moves(self) -> list:
        """ Get all moves a piece can take """
        moves = []

        if self.directions == 'straight':
            moves += self.get_straight_moves()
        elif self.directions == 'diagonal':
            moves += self.get_diagonal_moves()
        elif self.directions == 'all':
            moves += self.get_diagonal_moves()
            moves += self.get_straight_moves()

        return moves

    def get_straight_moves(self) -> list:
        return self._get_moves([0, 0, -1, 1], [-1, 1, 0, 0])

    def get_diagonal_moves(self) -> list:
        return self._get_moves([1, 1, -1, -1], [-1, 1, -1, 1])

    def _get_moves(self, xlist, ylist):
        moves = []
        xnum = self.board.get_x(self.x)
        ynum = self.y

        for x, y in zip(xlist, ylist):
            for num in range(1, (8 if self.distance == 0 else 2)):
                _x = xnum + x * num
                _y = ynum + y * num

                if self.board.tile_exists(_x, _y):
                    tile = self.board.tile(_x, _y)
                    if tile is None:
                        moves.append(self.board.str_pos(_x, _y))
                    elif tile.color != self.color:
                        moves.append(self.board.str_pos(_x, _y))
                        break
                    elif tile.color == self.color:
                        break

        return moves

    @property
    def str_pos(self):
        return f"{self.x}{self.y}"

    def __repr__(self) -> str:
        return f"<{self.color.capitalize()} {self.__class__.__name__} {self.str_pos}>"

class King(Piece):
    char = "k"
    directions = 'all'
    distance = 1
    value = 0

class Queen(Piece):
    char = "q"
    directions = 'all'
    distance = 0  # infinity
    value = 9

class Rook(Piece):
    char = 'r'
    directions = 'straight'
    distance = 0  # infinity
    value = 5

class Bishop(Piece):
    char = "b"
    directions = 'diagonal'
    distance = 0  # infinity
    value = 3

class Knight(Piece):
    char = 'h'  # H for horse
    value = 3

    def all_moves(self):
        xnum = self.board.get_x(self.x)
        ynum = self.y
        moves = []

        for x, y in zip([-1, 1, 2, 2, 1, -1, -2, -2], [2, 2, 1, -1, -2, -2, 1, -1]):
            _x = xnum + x
            _y = ynum + y

            if self.board.tile_exists(_x, _y):
                tile = self.board.tile(_x, _y)
                if tile is None:
                    moves.append(self.board.str_pos(_x, _y))
                elif tile.color != self.color:
                    moves.append(self.board.str_pos(_x, _y))
                    continue
                elif tile.color == self.color:
                    continue

        return moves

class Pawn(Piece):
    char = 'p'
    value = 1

    def all_moves(self):
        xnum = self.board.get_x(self.x)
        ynum = self.y
        moves = []

        # check in front
        _x = xnum
        for i in range(1, (2 if self.moved else 3)):
            if self.color == color.WHITE:
                i = i * -1
            _y = ynum + i

            if self.board.tile(_x, _y) is None:
                moves.append(self.board.str_pos(_x, _y))
            else:
                break

        # check diagonals
        _y = ynum + (1 if self.color == color.BLACK else -1)

        for i in [-1, 1]:
            _x = xnum + i
            if self.board.tile_exists(_x, _y):
                tile = self.board.tile(_x, _y)
                if tile is not None:
                    if tile.color != self.color:
                        moves.append(self.board.str_pos(_x, _y))

        return moves

    @property
    def moved(self):
        if self.color == color.WHITE and self.y == 6:
            return False
        if self.color == color.BLACK and self.y == 1:
            return False
        return True
