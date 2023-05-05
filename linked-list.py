class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None
    def print__ll(self):
        if self.head is None:
            print("empty")