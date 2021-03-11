from space import *


class FreeSpace(Space):
    def __init__(self, father, x_position, y_position):
        super().__init__(x_position, y_position)
        self.value = "_"
        self.distance = 0
        self.father = None


