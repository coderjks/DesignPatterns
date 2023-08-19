from cell import Cell
from random import randint
from snake_ladder import SnakeLadder


class Board:

    def __init__(self, _id, dim, no_of_snakes, no_of_ladders):
        self._id = _id
        self.dim = dim
        self.snakes = no_of_snakes
        self.ladders = no_of_ladders
        self.cells = None

    def initialize(self):
        self.cells = [[Cell() for _ in range(self.dim)] for _ in range(self.dim)]
        self.add_ladders_snakes()

    def get_cell(self, position):
        row = position % self.dim
        col = position // self.dim
        return self.cells[row][col]

    def add_ladders_snakes(self):
        snakes_added = 0
        while snakes_added < self.snakes:
            start = randint(0, (self.dim * self.dim) - 1)
            end = randint(0, (self.dim * self.dim) - 1)
            if start <= end:
                continue

            cell = self.get_cell(start)

            if not cell.snake_ladder:
                cell.snake_ladder = SnakeLadder(start, end)
                snakes_added += 1

        ladders_added = 0
        while ladders_added < self.ladders:
            start = randint(0, (self.dim * self.dim) - 1)
            end = randint(0, (self.dim * self.dim) - 1)
            if start >= end:
                continue

            cell = self.get_cell(start)

            if not cell.snake_ladder:
                cell.snake_ladder = SnakeLadder(start, end)
                ladders_added += 1
