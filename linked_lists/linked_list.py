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

    def find_middle_element(self):
        """ Move one pointer by one and other pointer by two.
        When the fast pointer reaches end slow pointer will reach middle of the linked list"""
        ptr1 = self.head
        ptr2 = self.head
        while ptr2 is not None and ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next  # will move by 2
        print("The middle element is [{}] \n".format(ptr1.data));

    def traverse(self, head_node):
        if head_node is not None:
            print(head_node.data)
            self.traverse(head_node.next)
