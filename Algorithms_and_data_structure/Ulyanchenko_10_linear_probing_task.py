"""
22/03/2026
@author: Ulyanchenko Ivan
"""


class MyHashTable:
    def __init__(self):
        self.slots = 10
        self.load_factor = 0.75
        self.head = [None] * self.slots

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        hash_value = self.hash_function(key)
        cells = self.head
        obj = (key, value)
        while True:
            current_cell = cells[hash_value]
            if current_cell is None:
                self.head[hash_value] = obj
                if sum(1 for cell in self.head if cell is not None) / self.slots >= self.load_factor:
                    self.rehashing()
                break
            elif current_cell[0] == obj[0]:
                self.head[hash_value] = obj
                break
            hash_value = (hash_value + 1) % self.slots
            if sum(1 for cell in self.head if cell is not None)/self.slots >= self.load_factor:
                self.rehashing()

    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """

    def rehashing(self):
        """
        increase the slots number if load factor is high.
        :return:
        """
        pass


if __name__ == '__main__':
    # your testing is here
    pass
