from space import *


class Pipeline(Space):
    def __init__(self, row_position, col_position):
        super().__init__(row_position, col_position)
        self.value = "🏁"


