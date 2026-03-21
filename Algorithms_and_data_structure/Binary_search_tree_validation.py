class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst_rec(node, lo, hi):
    if node is None:
        return True
    if (lo is None or lo < node.value) and (hi is None or node.value < hi):
        left = is_bst_rec(node.left, lo, node.value)
        right = is_bst_rec(node.right, node.value, hi)
        if left is True and right is True:
            return True
        else:
            return False
    return False


def is_bst_rec_inv(node, lo, hi):
    if node is None:
        return True
    if (lo is None or lo < node.value) and (hi is None or node.value < hi):
        left = is_bst_rec_inv(node.left, node.value, hi)
        right = is_bst_rec_inv(node.right, lo, node.value)
        return left and right
    return False


def is_bst(node):
    if node is None:
        return True
    lo, hi = None, None
    first = is_bst_rec(node, lo, hi)
    second = is_bst_rec_inv(node, hi, lo)
    if first is True or second is True:
        return True
    return False
