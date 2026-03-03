class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.count = 1
        self.left = None
        self.right = None


class KeyValueBST:
    def __init__(self):
        self._root = None

    def __iter__(self):
        self._iter_keys = self.keys()
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self._iter_keys):
            raise StopIteration
        current_key = self._iter_keys[self._iter_index]
        self._iter_index += 1
        return current_key

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def _put(self, node, key, val):
        if node is None:
            return Node(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def get(self, key):
        current_node = self._root
        while current_node is not None:
            if current_node.key > key:
                current_node = current_node.left
            elif current_node.key < key:
                current_node = current_node.right
            else:
                return current_node.value

    def delete(self, key):
        self._root = self._delete(self._root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            to_delete = node
            node = self._min_node(to_delete.right)
            node.right = self._delete_min(to_delete.right)
            node.left = to_delete.left
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _min_node(self, node):
        """Повертає сам вузол з найменшим ключем (йдемо наліво)"""
        if node.left is None:
            return node
        return self._min_node(node.left)

    def _delete_min(self, node):
        """Видаляє найменший вузол і повертає оновлене дерево"""
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def contains(self, key):
        return self.get(key) is not None

    def is_empty(self):
        return self._root is None

    def size(self, lo=None, hi=None):
        """
        should return the number of all keys if lo and hi are not passed.
        In other case, returns the number of keys between lo and hi
        :param lo:
        :param hi:
        :return:
        """
        if lo is None and hi is None:
            return self._size(self._root)

    def _size(self, node):
        if node is None:
            return 0
        return node.count

    def min(self):
        current_node = self._root
        if current_node is None:
            return None
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.key

    def max(self):
        current_node = self._root
        if current_node is None:
            return None
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.key

    def keys(self, lo=None, hi=None):
        """
        returns a list of all keys.
        If lo and hi are passed, returns a list of keys between lo and hi
        :param lo:
        :param hi:
        :return:
        """
        if self.is_empty():
            return []
        if lo is None:
            lo = self.min()
        if hi is None:
            hi = self.max()
        queue = []
        self._keys(self._root, queue, lo, hi)
        return queue

    def _keys(self, node, queue, lo, hi):
        if node is None:
            return
        if lo < node.key:
            self._keys(node.left, queue, lo, hi)
        if lo <= node.key <= hi:
            queue.append(node.key)
        if hi > node.key:
            self._keys(node.right, queue, lo, hi)

    def floor(self, key):
        """
        найбільший ключ менший або рівний key
        :param key:
        :return:
        """
        floor = self._floor(self._root, key)
        if floor is None:
            return None
        return floor.key

    def _floor(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key > key:
            return self._floor(node.left, key)
        else:
            better = self._floor(node.right, key)
            if better is not None:
                return better
            return node

    def ceiling(self, key):
        """
        найменший ключ більший або рівний key
        :param key:
        :return:
        """
        ceiling = self._ceiling(self._root, key)
        if ceiling is None:
            return None
        return ceiling.key

    def _ceiling(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key < key:
            return self._ceiling(node.right, key)
        else:
            better = self._ceiling(node.left, key)
            if better is not None:
                return better
            return node

    def rank(self, key):
        """
        кількість ключів менших за key
        :param key:
        :return:
        """
        return self._rank(key, self._root)

    def _rank(self, key, node):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(key, node.right)
        else:
            return self._size(node.left)

    def select(self, k):
        if k < 0 or k >= self.size():
            return None

        node = self._select(self._root, k)
        if node is not None:
            return node.key
        return None

    def _select(self, node, k):
        if node is None:
            return None
        left_size = self._size(node.left)
        if left_size > k:
            return self._select(node.left, k)
        elif left_size < k:
            return self._select(node.right, k - left_size - 1)
        else:
            return node

    def delete_min(self):
        if self._root is None:
            return None
        self._root = self._delete_min(self._root)

    def delete_max(self):
        if self._root is None:
            return None
        self._root = self._delete_max(self._root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left
        node.right = self._delete_max(node.right)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node
