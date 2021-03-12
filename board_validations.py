from free_space import *
from pipeline import *


class BoardValidations:


    @staticmethod
    def _is_a_valid_row(row, boar_dimensions):
        return 0 <= row < boar_dimensions.num_rows

    @staticmethod
    def _is_a_valid_col(col, boar_dimensions):
        return 0 <= col < boar_dimensions.num_cols

    @staticmethod
    def _is_a_valid_child(state, successor):
        return state.father != successor

    @staticmethod
    def _is_a_valid_distance_to_change(state, successor):
        return successor.distance == 0 or successor.distance > state.distance

    def is_a_valid_successor(self, successor, state):
        if isinstance(state, Pipeline):
            return True
        return self._is_a_valid_child(state, successor) and self._is_a_valid_distance_to_change(state, successor)

    def is_a_valid_space(self, position,  boar_dimensions):
        return self._is_a_valid_row(position.row, boar_dimensions) and self._is_a_valid_col(position.col, boar_dimensions)
