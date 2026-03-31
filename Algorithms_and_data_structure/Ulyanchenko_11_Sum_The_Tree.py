class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def _sum_the_tree_values(node):
    list_of_values = []
    if node:
        list_of_values.append(node.val)
        list_of_values += _sum_the_tree_values(node.left)
        list_of_values += _sum_the_tree_values(node.right)
    return list_of_values


def sum_the_tree_values(node):
    return sum(_sum_the_tree_values(node))
