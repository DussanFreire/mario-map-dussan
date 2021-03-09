from BoardDimensions import *
import FreeSpace


class Board:
    @staticmethod
    def _create_board(num_rows, num_cols):
        matrix = []
        for row in range(0, num_rows):
            matrix.append([])
            for col in range(0, num_cols):
                matrix[row].append(1)
        return matrix

    def __init__(self, num_rows, num_cols):
        self.dimensions = BoardDimensions(num_rows, num_cols)
        self.board = Board._create_board(num_rows, num_cols)

    def show_board(self):
        for line in self.board:
            print(*line)


a = Board(5, 5)
a.show_board()

