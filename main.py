from board import Board
from position import *

if __name__ == "__main__":
    a = Board(8, 8)
    a._add_pipelines(Position(7, 7))
    a._mark_distances()

    print(a.get_html_board())

