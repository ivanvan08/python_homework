class Node:
    def __init__(self, next=None):
        self.next = next


def swap_head(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    current = head
    prev = current
    counter = 1
    while current is not None and current.next is not None:
        second = current.next
        if counter == 1:
            our_head = second
            counter = 0
        prev.next = second
        next_pair_first = second.next
        current.next = next_pair_first
        second.next = current
        prev = current
        current = current.next
    return our_head

