from dimensions import *
from wall import *
from free_space import *
from pipeline import *
from settings import *
from agent import *
from board_validations import *
import queue


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
        self.settings = Settings()
        self.agent = Agent(self.settings)
        self.board_validations = BoardValidations()

    def show_board(self):
        for line in self.board:
            for elem in line:
                print(elem.distance if isinstance(elem, FreeSpace) else elem.value, end="\t")
            print()
        print()

    def add_pipelines(self, *pipeline_positions):
        for position in pipeline_positions:
            self.board[position.row][position.col] = Pipeline(position.row, position.col)

    def add_walls(self, *wall_positions):
        for position in wall_positions:
            self.board[position.row][position.col] = Wall(position.row, position.col)

    def _load_default_board(self):
        # self.add_pipelines(Position(0, 3), Position(3, 0))
        # self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3))
        self.add_pipelines(Position(0, 3), Position(3, 0), Position(3, 4), Position(6, 0), Position(7, 7))
        self.add_walls(Position(0, 1), Position(2, 1), Position(3, 1), Position(1, 3), Position(2, 3), Position(2, 2), Position(3, 3))
        self.show_board()

    def find_pipelines(self):
        for row in self.board:
            for element in row:
                if isinstance(element, Pipeline):
                    self.mark_island_as_visited_bfs(element.position)

    def _discard_successors(self, successors_positions, state_position):
        state = self.board[state_position.row][state_position.col]
        filtered_successors = []
        for successor_position in successors_positions:
            if self.board_validations.is_a_valid_space(successor_position, self.boar_dimensions) and \
                    isinstance(self.board[successor_position.row][successor_position.col], FreeSpace) and \
                    self.board_validations.is_a_valid_successor(self.board[successor_position.row][successor_position.col], state):
                filtered_successors.append(successor_position)
        return filtered_successors
        # return filter(lambda x: self._is_a_valid_successor(x), successors)

    def _mark_successors_distance(self, successors_positions, state_position):
        state = self.board[state_position.row][state_position.col]
        for successor_position in successors_positions:
            successor = self.board[successor_position.row][successor_position.col]
            successor.distance = 1 if isinstance(state, Pipeline) else state.distance + 1
            successor.father = state

    def mark_island_as_visited_bfs(self, position):
        open = queue.SimpleQueue()
        close = []

        open.put(position)
        while open.qsize() != 0:
            state_position = open.get()
            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors_positions = self.agent.transition_function(state_position, actions)
            successors_positions = self._discard_successors(successors_positions, state_position)
            self._mark_successors_distance(successors_positions, state_position)
            self.show_board()
            close.append(state_position)

            for successor_position in successors_positions:
                open.put(successor_position)


a = Board(8, 8)
# print(a._is_a_valid_successor(Position(1, 4)),a.dimensions.num_rows)
a.find_pipelines()
# a = Board(4, 4)
# a.add_pipelines(Position(0, 3), Position(3, 0))
# a.add_walls(Position(0, 1), Position(2, 1), Position(3, 1),Position(1, 3), Position(2, 3))
# a.show_board()
