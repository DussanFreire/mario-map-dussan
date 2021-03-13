from wall import *
from board_distance_finder import *
from dimensions import *


class Board:
    @staticmethod
    def _create_board(num_rows, num_cols):
        matrix = []
        for row in range(0, num_rows):
            matrix.append([])
            for col in range(0, num_cols):
                matrix[row].append(FreeSpace())
        return matrix

    def __init__(self, num_rows, num_cols):
        self.boar_dimensions = BoardDimensions(num_rows, num_cols)
        self.board = Board._create_board(num_rows, num_cols)
        self._load_default_board()

    def add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.row][position.col] = Pipeline(position.row, position.col)

    def add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.row][position.col] = Wall()

    def _load_default_board(self):
        # self.add_pipelines(Position(0, 3), Position(3, 0))
        # self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3))
        self.add_pipelines(Position(0, 3), Position(3, 0), Position(3, 4), Position(6, 0), Position(7, 7))
        self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3), Position(2, 2), Position(3, 3))

    def mark_distances(self):
        BoardDistanceFinder.mark_distances(self.board, self.boar_dimensions)
