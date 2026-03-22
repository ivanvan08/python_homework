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
