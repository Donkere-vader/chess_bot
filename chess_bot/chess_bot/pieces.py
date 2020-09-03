
class color:
    BLACK = 'black'
    WHITE = 'white'

class Piece:
    def __init__(self, game, x, y, color):
        self.game = game  # parent game
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.x}, {self.y})>"

class King(Piece):
    char = "k"

class Queen(Piece):
    char = "q"

class Bishop(Piece):
    char = "b"

class Knight(Piece):
    char = 'h'  # H for horse

class Rook(Piece):
    char = 'r'

class Pawn(Piece):
    char = 'p'
