class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self._size = 0

    def insert_to_start(self, data):
        """
        add a node at begin of linked-list
        :param data:
        :return:
        """
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node.next = self.head_node
            self.head_node.prev = new_node
            self.head_node = new_node
        self._size += 1

    def insert_to_end(self, data):
        """
        add a node at the end of linked-list
        :param data:
        :return:
        """
        new_node = Node(data)
        if self.tail_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node.prev = self.tail_node
            self.tail_node.next = new_node
            self.tail_node = new_node
        self._size += 1

    def remove_head(self):
        """
        remove first node of linked list
        :return:
        """
        if self.tail_node is None:
            return None
        first_node_data = self.head_node.data
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
            self._size -= 1
            return first_node_data
        self.head_node = self.head_node.next
        self.head_node.prev.next = None
        self.head_node.prev = None
        self._size -= 1
        return first_node_data

    def remove_tail(self):
        """
        remove last node of linked list
        :return:
        """
        if self.tail_node is None:
            return None
        last_node_data = self.tail_node.data
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
            self._size -= 1
            return last_node_data
        self.tail_node = self.tail_node.prev
        self.tail_node.next.prev = None
        self.tail_node.next = None
        self._size -= 1
        return last_node_data

    def size(self) -> int:
        """
        return size of linked list
        :return: int
        """
        return self._size

    def show(self):
        """
        print linked list
        :return:
        """
        output = []
        current_node = self.head_node
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        print(output)


class Stack:
    def __init__(self):
        self.container = DoublyLinkedList()

    def empty(self):
        if self.container.size() == 0:
            return True
        return False

    def size(self):
        return self.container.size()

    def top(self):
        if self.container.tail_node:
            return self.container.tail_node.data
        return None

    def push(self, data):
        self.container.insert_to_end(data)

    def pop(self):
        return self.container.remove_tail()

    def __iter__(self):
        current = self.container.tail_node
        while current:
            yield current.data
            # must be waiting here before next step
            current = current.prev


class Queue:
    def __init__(self):
        self.container = DoublyLinkedList()

    def is_empty(self):
        if self.container.size() == 0:
            return True
        return False

    def size(self):
        return self.container.size()

    def enqueue(self, data):
        self.container.insert_to_end(data)

    def dequeue(self):
        return self.container.remove_head()

    def __iter__(self):
        current = self.container.head_node
        while current:
            yield current.data
            # must be waiting here before next step
            current = current.next


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.insert_to_end('a')
    doubly_linked_list.insert_to_end('b')
    doubly_linked_list.insert_to_start('c')
    doubly_linked_list.insert_to_start('abc')
    doubly_linked_list.insert_to_start(32)
    doubly_linked_list.insert_to_start(['a', '32', 32])
    doubly_linked_list.insert_to_start((['a'], 12))
    doubly_linked_list.show()
    print(doubly_linked_list.size())
    doubly_linked_list.insert_to_end('d')

    print("Node Data")
    doubly_linked_list.show()

    print("Remove First Node")
    doubly_linked_list.remove_head()
    print("Remove Last Node")
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()

    print("Linked list after removing a node:")
    doubly_linked_list.show()

    print("Size of linked list :", end=" ")
    print(doubly_linked_list.size())
