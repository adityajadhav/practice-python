from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def set_head(self, head_node):
        self.head = head_node

    # Pushes an item on the front of the list.
    def push(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.head = node

    def traverse(self, head_node):
        if head_node is not None:
            print(head_node.data)
            self.traverse(head_node.next)
