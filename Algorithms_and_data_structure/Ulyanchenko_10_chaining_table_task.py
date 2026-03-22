class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.next = None

    def __str__(self):
        return f"{self.key}: {self.value} -> {self.next}"


class MyHashTable:
    def __init__(self):
        self.slots = 10
        self.load_factor = 0.75
        self.st = [None] * self.slots
        self.number_of_taken_slots = 0

    def __str__(self):
        return "  |  ".join(map(str, self.st))

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value) -> ListNode:
        """
        :param key:
        :param value:
        :return:
        """
        if self.number_of_taken_slots >= self.slots * self.load_factor:
            self.rehashing()
        key_hash = self.hash_function(key)
        if self.st[key_hash] is None:
            node = ListNode(key, value)
            self.st[key_hash] = node
            self.number_of_taken_slots += 1
            return node
        else:
            current_node = self.st[key_hash]
            while current_node:
                if key == current_node.key:
                    current_node.value = value
                    return current_node
                current_node = current_node.next
            node = ListNode(key, value)
            tail = self.st[key_hash]
            node.next = tail
            self.st[key_hash] = node
            return node

    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """
        key_hash = self.hash_function(key)
        current_node = self.st[key_hash]
        while current_node:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next
        return None

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """
        key_hash = self.hash_function(key)
        current_node = self.st[key_hash]
        if current_node is None:
            return None
        elif current_node.key == key:
            self.st[key_hash] = current_node.next
            return None
        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return None

    def rehashing(self):
        """
        increase the slots number if load factor is high.
        :return:
        """
        old_list = self.st
        self.slots *= 2
        self.st = [None] * self.slots
        self.number_of_taken_slots = 0
        for i in old_list:
            if i:
                while i.next:
                    self.put(i.key, i.value)
                    i = i.next
                self.put(i.key, i.value)


if __name__ == '__main__':
    obj = MyHashTable()
    obj.put("1", 1)
    obj.put("1", 2)
    obj.put("2", 27)
    obj.put("3", 12)
    obj.put("4", 2)
    obj.put("14", 22)
    obj.put("24", 2)

    print(obj)
    print(obj.get("1"))
    print(obj.get("14"))
    print(obj.get("24"))

    obj.remove("1")
    obj.remove("2")
    obj.remove("14")
    print(obj)
