class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None
    def print__ll(self):
        if self.head is None:
            print("empty linked list")

        else:
            n = self.head
            while n is not None:
                print(n.data) 
                n = n.ref
    def add_begin(self, data):
        new_node = Node (data)
        new_node.ref == self.head
        self.head = new_node

llst1 = LinkedList()

llst1.add_begin(20)
llst1.add_begin(50)

llst1.print__ll()