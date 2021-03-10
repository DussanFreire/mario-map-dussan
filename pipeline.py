from space import *


class Pipeline(Space):
    def __init__(self, x_position, y_position):
        super().__init__(x_position, y_position)
        self.value = "🏁"


