from dimensions import *
from wall import *
from free_space import *
from pipeline import *
# import numpy


class Board:
    @staticmethod
    def _create_board(num_rows, num_cols):
        matrix = []
        for row in range(0, num_rows):
            matrix.append([])
            for col in range(0, num_cols):
                matrix[row].append(FreeSpace(None, row, col))
        return matrix

    def __init__(self, num_rows, num_cols):
        self.dimensions = BoardDimensions(num_rows, num_cols)
        self.board = Board._create_board(num_rows, num_cols)
        self._load_default_board()

    def show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.value, end="\t")
            print()

    def add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.x_position][position.y_position] = Pipeline(position.x_position, position.y_position)

    def add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.x_position][position.y_position] = Wall(position.x_position, position.y_position)

    def _load_default_board(self):
        self.add_pipelines(Position(0, 3), Position(3, 0))
        self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1),Position(1, 3), Position(2, 3))
        self.show_board()


a = Board(4, 4)
# a = Board(4, 4)
# a.add_pipelines(Position(0, 3), Position(3, 0))
# a.add_walls(Position(0, 1), Position(2, 1), Position(3, 1),Position(1, 3), Position(2, 3))
# a.show_board()
