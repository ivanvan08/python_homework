class ListNode:
    def __init__(self, object):
        self.object = self
        self.connected = None


class dinamic_link:
    def __init__(self):
        self.root = None
        self.count_connections = 0
        self.list_connected = []

    def union(self, object_1, object_2):
        current_node = ListNode(object_1)
        self.root = current_node
        node_to_link = ListNode(object_2)
        current_node.connected = node_to_link
        node_to_link.connected = current_node
        connected_node = current_node.connected
        current_node.list_connected.append(connected_node)
        node_to_link.list_connected.append(node_to_link.connected)

    def connected(self, object_1, object_2):
        if object_2 in object_1.list_connected:
            return True
        return False

    # def count(self):


