class Percolation:
    def __init__(self, number: int):
        """
        create NxN matrix with all closed cells
        :param number: <int> number of rows and columns
        """
        self.matrix = [[False for j in range(number)] for k in range(number)]
        self.parent = [j for j in range(number) + 2]
        self.top = number * number
        self.bottom = number * number + 1
        for j in range(number):
            union(TOP, j)

        for j in range(number):
            union(BOTTOM, number * (number - 1) + j)

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
        ...

    def is_opened(self, i: int, j: int) -> bool:
        """
        check if cell is opened yet
        :param i: <int> row index
        :param j: <int> column index
        :return: <bool> is cell opened
        """

    def percolates(self) -> bool:
        """
        check if system percolates
        :return: <bool> percolates
        """
