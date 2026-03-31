"""
30/03/2026
@author: Ulyanchenko Ivan
"""
# import time

from percolation import Percolation


class PercolationExperiment:
    def __init__(self, n: int, t: int):
        """
        run T separate experiments with NxN matrix
        :param n: <int> number of rows and columns in matrix
        :param t: <int> number of experiments
        """
        self.results = []
        for i in range(t):
            per = Percolation(n)
            while not per.percolates():
                per.open()
            self.results.append(per.opened_count() / (n ** 2))
        self.length = len(self.results)

    def mean(self) -> float:
        return sum(self.results) / self.length

    def std(self) -> float:
        all_sqr = []
        mean = self.mean()
        for i in self.results:
            all_sqr.append((i - mean) ** 2)
        return (sum(all_sqr) / (self.length - 1)) ** 0.5

    def confidence_interval(self) -> (float, float):
        std = self.std()
        mean = self.mean()
        return (mean - (1.96 * std / self.length ** 0.5)), (mean + (1.96 * std / self.length ** 0.5))


def main():
    """
    run experiments and compute mean, std, confidence interval.
    print results on screen in readable format.
    """
    # beginning = time.time()
    n = 200
    t = 100
    exp = PercolationExperiment(n, t)
    mean = exp.mean()
    std = exp.std()
    confidence_interval = exp.confidence_interval()
    # time_spend = time.time()-beginning
    print(f"""    кількість стовпців і рядків в матриці: {n}
    кількість експериментів: {t}
    середнє арифметичне: {mean}
    стандартне відхилення: {std}
    кількість клітинок які треба відкрити (не в відсотках): {confidence_interval[0]*100, confidence_interval[1]*100}""")


if __name__ == "__main__":
    main()
