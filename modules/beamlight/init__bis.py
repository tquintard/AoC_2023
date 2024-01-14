from math import *


class Grid:
    def __init__(self, inputs: list) -> None:
        self.dimx, self.dimy = len(inputs[0]), len(inputs)
        self.grid, self.visu = list(), list()
        for line in inputs:
            self.grid.append(list(line))
            # self.visu.append(list(line))
            # self.visu.append(list('.'*len(line)))
        self.visited = set()
        self.actual = tuple()
        self.orient = None
        self.queue = list()

    def get_data(self, x: int, y: int) -> str:
        return self.grid[y][x]

    def set_data(self, x: int, y: int, data: str) -> None:
        self.visu[y][x] = data

    def next_tile(self, dx: int = 0, dy: int = 0, dO: int = 0) -> tuple:
        actual = (self.actual[0] + dx, self.actual[1] + dy)
        orient = self.orient + dO
        return actual, orient

    def print(self) -> None:
        for line in self.visu:
            print(''.join(line))

    def move_beam(self):
        cos_a, sin_a = (int(cos(self.orient)), int(sin(self.orient)))
        if 0 <= self.actual[0] < self.dimx \
                and 0 <= self.actual[1] < self.dimy \
                and (self.actual, cos_a, sin_a) not in self.visited:
            element = self.get_data(*self.actual)

            # self.set_data(*self.actual, '#')
            self.visited.add((self.actual, cos_a, sin_a))

            if element == '.':
                self.actual, self.orient = self.next_tile(cos_a, -sin_a)
                self.move_beam()
            elif element == '/':
                if sin_a == 0:
                    dy, dO = -cos_a, pi/2
                    self.actual, self.orient = self.next_tile(dy=dy, dO=dO)
                    self.move_beam()
                else:
                    dx, dO = sin_a, -pi/2
                    self.actual, self.orient = self.next_tile(dx=dx, dO=dO)
                    self.move_beam()
            elif element == '\\':
                if sin_a == 0:
                    dy, dO = cos_a, -pi/2
                    self.actual, self.orient = self.next_tile(dy=dy, dO=dO)
                    self.move_beam()
                else:
                    dx, dO = -sin_a, pi/2
                    self.actual, self.orient = self.next_tile(dx=dx, dO=dO)
                    self.move_beam()
            elif element == '|':
                if cos_a == 0:
                    dy = -sin_a
                    self.actual, self.orient = self.next_tile(dy=dy)
                    self.move_beam()
                else:
                    self.queue.__delitem__(0)
                    for coef in range(-1, 2, 2):
                        actual = self.actual[0], self.actual[1] + coef
                        orient = -coef*pi/2
                        self.queue.append((actual, orient))
            elif element == '-':
                if sin_a == 0:
                    dx = cos_a
                    self.actual, self.orient = self.next_tile(dx=dx)
                    self.move_beam()
                else:
                    self.queue.__delitem__(0)
                    for coef in range(-1, 2, 2):
                        actual = self.actual[0] + coef, self.actual[1]
                        orient = (1-coef)*pi/2
                        self.queue.append((actual, orient))
        else:
            self.queue.__delitem__(0)
