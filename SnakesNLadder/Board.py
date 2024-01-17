import random
from SnakesNLadder.Cell import Cell
from SnakesNLadder.Jump import Jump


# class Cell:
#     def __init__(self):
#         self.jump = None
#
# class Jump:
#     def __init__(self):
#         self.start = 0
#         self.end = 0

class Board:
    def __init__(self, board_size, num_snakes, num_ladders):
        self.cells = []
        self.initialize_cells(board_size)
        self.add_snakes_ladders(num_snakes, num_ladders)

    def initialize_cells(self, board_size):
        self.cells = [[Cell() for _ in range(board_size)] for _ in range(board_size)]

    def add_snakes_ladders(self, num_snakes, num_ladders):
        while num_snakes > 0:
            snake_head = random.randint(1, len(self.cells) * len(self.cells) - 1)
            snake_tail = random.randint(1, len(self.cells) * len(self.cells) - 1)

            if snake_tail >= snake_head:
                continue

            snake_obj = Jump()
            snake_obj.start = snake_head
            snake_obj.end = snake_tail

            cell = self.get_cell(snake_head)
            cell.jump = snake_obj

            num_snakes -= 1

        while num_ladders > 0:
            ladder_start = random.randint(1, len(self.cells) * len(self.cells) - 1)
            ladder_end = random.randint(1, len(self.cells) * len(self.cells) - 1)

            if ladder_start >= ladder_end:
                continue

            ladder_obj = Jump()
            ladder_obj.start = ladder_start
            ladder_obj.end = ladder_end

            cell = self.get_cell(ladder_start)
            cell.jump = ladder_obj

            num_ladders -= 1

    def get_cell(self, player_position):
        board_row = player_position // len(self.cells)
        board_column = player_position % len(self.cells)
        return self.cells[board_row][board_column]

# # Example usage
# board_size = 10
# num_snakes = 5
# num_ladders = 5
#
# snake_ladder_board = Board(board_size, num_snakes, num_ladders)
