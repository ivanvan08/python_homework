"""
06/04/2026
@author: Ulyanchenko Ivan
"""


# n = int(input())
# matrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# used in web tests


def check(n, matrix):
    for row in range(n):
        for column in range(n):
            if row == column and matrix[row][column] == 1:
                return print("NO")
            elif matrix[row][column] != matrix[column][row]:
                return print("NO")
    return print("YES")


check(3, [[0, 1, 1], [1, 0, 1], [1, 1, 0]])  # YES
check(3, [[0, 1, 1], [1, 0, 1], [0, 1, 0]])  # NO
check(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # NO
check(1, [[0]])  # YES
check(1, [[1]])  # NO
check(2, [[0, 1], [1, 0]])  # YES
check(2, [[0, 0], [0, 0]])  # YES
