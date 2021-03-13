from board_validations import *
import queue
from settings import *
from agent import *


class BoardDistanceFinder:

    settings = Settings()
    agent = Agent(settings)

    @staticmethod
    def show_board(board):
        for line in board:
            for elem in line:
                print(elem.distance if isinstance(elem, FreeSpace) else elem.value, end="\t")
            print()
        print()

    @staticmethod
    def mark_distances(board, boar_dimensions):
        for row in board:
            for element in row:
                if isinstance(element, Pipeline):
                    BoardDistanceFinder._mark_distance_in_the_board_bfs(board, element.position, boar_dimensions)

    @staticmethod
    def _discard_successors(board, boar_dimensions, successors_positions, state_position):
        filtered_successors = []
        for successor_position in successors_positions:
            if BoardValidations.is_a_successor(board, state_position, successor_position, boar_dimensions):
                filtered_successors.append(successor_position)
        return filtered_successors

    @staticmethod
    def _mark_successors_distance(board, successors_positions, state_position):
        state = board[state_position.row][state_position.col]
        for successor_position in successors_positions:
            successor = board[successor_position.row][successor_position.col]
            successor.distance = 1 if isinstance(state, Pipeline) else state.distance + 1
            successor.father = state

    @staticmethod
    def _mark_distance_in_the_board_bfs(board, position, boar_dimensions):
        open = queue.SimpleQueue()
        close = []

        open.put(position)
        while open.qsize() != 0:
            state_position = open.get()

            actions = [BoardDistanceFinder.settings.UP, BoardDistanceFinder.settings.DOWN, BoardDistanceFinder.settings.LEFT, BoardDistanceFinder.settings.RIGHT]
            successors_positions = BoardDistanceFinder.agent.transition_function(state_position, actions)
            successors_positions = BoardDistanceFinder._discard_successors(board, boar_dimensions, successors_positions, state_position)
            BoardDistanceFinder._mark_successors_distance(board, successors_positions, state_position)
            close.append(state_position)

            for successor_position in successors_positions:
                open.put(successor_position)
        # BoardDistanceFinder.show_board(board)