from wall import *
from board_distance_finder import *
from dimensions import *
from mario import Mario


class Board:
    @staticmethod
    def _create_board(num_rows, num_cols):
        matrix = []
        for row in range(0, num_rows):
            matrix.append([])
            for col in range(0, num_cols):
                matrix[row].append(FreeSpace())
        return matrix

    def __init__(self):
        self.boar_dimensions =None
        self.board = None
        # self.boar_dimensions = BoardDimensions(num_rows, num_cols)
        # self.board = self._create_board(num_rows, num_cols)
        self.mario = None

    def init_board(self, num_rows, num_cols):
        matrix = []
        for row in range(0, num_rows):
            matrix.append([])
            for col in range(0, num_cols):
                matrix[row].append(FreeSpace())
        self.boar_dimensions = BoardDimensions(num_rows, num_cols)
        self.board = matrix

    def add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.row][position.col] = Pipeline(position.row, position.col)

    def add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.row][position.col] = Wall()

    def add_mario(self, position):
        if self.mario is not None:
            self.board[self.mario.position.row][self.mario.position.col] = FreeSpace()
        self.mario = Mario()
        self.mario.position = position
        self.board[self.mario.position.row][self.mario.position.col] = self.mario

    def _load_default_board(self):
        # self.add_pipelines(Position(0, 3), Position(3, 0))
        # self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3))
        self.add_pipelines(Position(0, 3), Position(3, 0), Position(3, 4), Position(6, 0), Position(7, 7))
        self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3), Position(2, 2),
                       Position(3, 3))

    def mark_distances(self):
        BoardDistanceFinder.mark_distances(self.board, self.boar_dimensions)

    def find_shortest_path(self):
        if self.mario is not None:
            return BoardDistanceFinder.find_shortest_path(self.board, self.mario.position, self.boar_dimensions)
        return None

    def get_html_board(self):
        tabla = "<head> <table style='background-color:black;'>"
        tabla += "<tr><td></td>"
        for col in range(0, self.boar_dimensions.num_cols):
            tabla += "<td width=20 border=1 style=' border-color: black;color: white; background-color: black;text-align:center;'>" + str(
                col + 1) + "</td>"
        tabla += "</tr>"
        for row in range(0, self.boar_dimensions.num_rows):
            tabla += "<tr>"
            tabla += "<td width=20 border=1 style='border-color: black;color: white; background-color: black;text-align:center;'>" + str(
                row + 1) + "</td>"
            for col in range(0, self.boar_dimensions.num_cols):
                value = self.board[row][col].distance if isinstance(self.board[row][col], FreeSpace) else self.board[row][
                    col].value
                tabla += "<td width=20 border=1 style='border-color: black;color: black; background-color: " + self.board[row][col].color + ";text-align:center;'>" + str(
                    value) + "</td>"
            tabla += "</tr>"
        tabla += "</table> </head>"
        return tabla

    def show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.distance if isinstance(elem, FreeSpace) else elem.value, end="\t")
            print()
        print()


# a = Board()
# a.init_board(4, 4)
# print(a.boar_dimensions.num_cols)
# a.add_pipelines(Position(0, 0))
# a.mark_distances()
# a.add_mario(Position(1, 1))
# a.show_board()
# print(a.find_shortest_path())
# a.add_mario(Position(2, 2))
# a.mark_distances()
# a.find_shortest_path()
# print(a.find_shortest_path())



a = Board()
a.init_board(10, 10)
print(a.boar_dimensions.num_cols)
a.add_pipelines(Position(0, 0))
print(a.show_board())
