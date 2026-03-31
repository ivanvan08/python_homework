class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def compare(a, b):
    if a and b:
        if a.val == b.val:
            a_left = a.left
            b_left = b.left
            first = compare(a_left, b_left)
            a_right = a.right
            b_right = b.right
            second = compare(a_right, b_right)
            if first is True and second is True:
                return True
    elif a is None and b is None:
        return True
    return False
