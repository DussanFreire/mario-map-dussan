from dimensions import *
from wall import *
from free_space import *
from pipeline import *
from position import *
from settings import *
from agent import *
import queue


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
        self.settings = Settings()
        self.agent = Agent(self.settings)

    def show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.distance if isinstance(elem, FreeSpace) else elem.value, end="\t")
            print()
        print()

    def add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.row][position.col] = Pipeline(position.row,
                                                              position.col)

    def add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.row][position.col] = Wall(position.row,
                                                          position.col)

    def _load_default_board(self):
        self.add_pipelines(Position(0, 3), Position(3, 0))
        self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3))
        self.show_board()

    def find_pipelines(self):
        for row in self.board:
            for element in row:
                if isinstance(element, Pipeline):
                    self.mark_island_as_visited_bfs(element.position)

    def is_a_valid_successor(self, successor, state,distance):
        if isinstance(self.board[state.row][state.col], Pipeline):
            return True
        return self.board[state.row][state.col].father != self.board[successor.row][successor.col] and self.board[successor.row][successor.col].distance == 0 or self.board[successor.row][successor.col].distance > distance

    def _discard_successors(self, successors, state,distance):
        filtered_successors = []
        for successor in successors:
            if self._is_a_valid_space(successor) and self.is_a_valid_successor(successor, state,distance):
                filtered_successors.append(successor)
        return filtered_successors
        # return filter(lambda x: self._is_a_valid_successor(x), successors)

    def _is_a_valid_row(self, row):
        return 0 <= row < self.dimensions.num_rows

    def _i_a_valid_col(self, col):
        return 0 <= col < self.dimensions.num_cols

    def _is_a_valid_space(self, position):
        return self._is_a_valid_row(position.row) and self._i_a_valid_col(position.col) and isinstance(
            self.board[position.row][position.col], FreeSpace)

    def _mark_successors_distance(self, positions, distance, state):
        for p in positions:
            self.board[p.row][p.col].distance = distance
            self.board[p.row][p.col].father = self.board[state.row][state.col]

    def mark_island_as_visited_bfs(self, position):
        open = queue.SimpleQueue()
        close = []
        distance = 1

        open.put(position)

        while open.qsize() != 0:
            state = open.get()

            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors = self.agent.transition_function(state, actions)
            successors = self._discard_successors(successors, state, distance)
            self._mark_successors_distance(successors, distance, state)
            distance += 1
            self.show_board()
            close.append(state)

            for successor in successors:
                open.put(successor)


a = Board(4, 4)
# print(a._is_a_valid_successor(Position(1, 4)),a.dimensions.num_rows)
a.find_pipelines()
# a = Board(4, 4)
# a.add_pipelines(Position(0, 3), Position(3, 0))
# a.add_walls(Position(0, 1), Position(2, 1), Position(3, 1),Position(1, 3), Position(2, 3))
# a.show_board()
