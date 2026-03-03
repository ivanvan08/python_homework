class KeyValueFull:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def put(self, key, val):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass

    def contains(self, key):
        pass

    def is_empty(self):
        pass

    def size(self, lo=None, hi=None):
        """
        should return the number of all keys if lo and hi are not passed.
        In other case, returns the number of keys between lo and hi
        :param lo:
        :param hi:
        :return:
        """
        pass

    def min(self):
        pass

    def max(self):
        pass

    def keys(self, lo=None, hi=None):
        """
        returns a list of all keys.
        If lo and hi are passed, returns a list of keys between lo and hi
        :param lo:
        :param hi:
        :return:
        """

    def floor(self, key):
        """
        найбільший ключ менший або рівний key
        :param key:
        :return:
        """
        pass

    def ceiling(self, key):
        """
        найменший ключ більший або рівний key
        :param key:
        :return:
        """
        pass

    def rank(self, key):
        """
        кількість ключів менших за key
        :param key:
        :return:
        """
        pass

    def select(self, k):
        pass

    def delete_min(self):
        pass

    def delete_max(self):
        pass
