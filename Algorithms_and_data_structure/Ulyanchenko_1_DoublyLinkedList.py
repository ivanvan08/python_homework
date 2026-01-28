class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert_to_start(self, data):
        """
        add a node at begin of linked-list
        :param data:
        :return:
        """
        pass

    def insert_to_end(self, data):
        """
        add a node at the end of linked-list
        :param data:
        :return:
        """
        pass

    def remove_head(self):
        """
        remove first node of linked list
        :return:
        """
        pass

    def remove_tail(self):
        """
        remove last node of linked list
        :return:
        """
        pass

    def size(self) -> int:
        """
        return size of linked list
        :return: int
        """
        pass

    def show(self):
        """
        print linked list
        :return:
        """
        pass


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.insert_to_end('a')
    doubly_linked_list.insert_to_end('b')
    doubly_linked_list.insert_to_start('c')
    doubly_linked_list.insert_to_end('d')

    print("Node Data")
    doubly_linked_list.show()

    print("Remove First Node")
    doubly_linked_list.remove_head()
    print("Remove Last Node")
    doubly_linked_list.remove_tail()

    print("Linked list after removing a node:")
    doubly_linked_list.show()

    print("Size of linked list :", end=" ")
    print(doubly_linked_list.size())
