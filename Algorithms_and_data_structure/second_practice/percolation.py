import random


class Percolation:
    def __init__(self, number: int):
        """
        create NxN matrix with all closed cells
        :param number: <int> number of rows and columns
        """
        self.matrix = [[False for j in range(number)] for k in range(number)]
        self.linked = [j for j in range(number * number + 2)]
        self.top = number * number
        self.bottom = number * number + 1
        self.number = number

    def _find(self, x):
        current = x
        while self.linked[current] != current:
            current = self.linked[current]
        return current

    def _union(self, x, y):
        parent_a = self._find(x)
        parent_b = self._find(y)
        self.linked[parent_a] = parent_b
        return True

    def opened_count(self) -> int:
        """
        opened cells count
        :return: <int> opened cells count
        """
        ...

    def open(self):
        """
        open random cell if it is not opened yet
        """
        cell = self._pick_random()
        self.matrix[cell[0]][cell[1]] = True
        new_index = cell[0] * self.number + cell[1]
        if cell[0] == 0:
            self._union(new_index, self.top)
        elif cell[0] == self.number - 1:
            self._union(new_index, self.bottom)
        neighbours = [
            (cell[0] - 1, cell[1]),
            (cell[0] + 1, cell[1]),
            (cell[0], cell[1] - 1),
            (cell[0], cell[1] + 1)
        ]
        for n_i, n_j in neighbours:
            if 0 <= n_i < self.number and 0 <= n_j < self.number:
                if self.matrix[n_i][n_j] is True:
                    self._union(n_i * self.number + n_j, new_index)

    def _pick_random(self):
        cell = random.randint(0, self.number - 1), random.randint(0, self.number - 1)
        if not self.matrix[cell[0]][cell[1]]:
            return cell
        else:
            return self._pick_random()

    def is_opened(self, i: int, j: int) -> bool:
        """
        check if cell is opened yet
        :param i: <int> row index
        :param j: <int> column index
        :return: <bool> is cell opened
        """
        return self.matrix[i][j]

    def percolates(self) -> bool:
        """
        check if system percolates
        :return: <bool> percolates
        """
