class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# creating linked list
class LinkedList:
    def __init__(self):
        self.head = None
    def print__ll(self):
        if self.head is None:
            print("empty linked list")

        else:
            n = self.head
            while n is not None:
                print(n.data, "--->",end=" ") 
                n = n.ref
# adding elements from the begining of the list
    def add_begin(self, data):
        new_node = Node (data)
        new_node.ref == self.head
        self.head = new_node

# adding elements from the begining of the list
    def add_end(self, data):
        new_node = Node (data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

# adding element between two nodes
    def add_between(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("node not present in the linkedlist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

# adding elements before a certain given node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref        
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node     

# adding items to an empty list
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

# deleting element from the begining of the list
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
            return
        else:
            self.head=self.head.ref

# delete the last element
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty can't delete!")
            return
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

# deleting by specified value
    def delete_by_value(self,x):
        if self.head is None:
            print("Linked List is empty can't delete!")
            return
        if x==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("node is not present in the ll")
        else:
            n.ref=n.ref.ref
    

llst1 = LinkedList()

llst1.add_begin(20)
llst1.add_begin(50)
llst1.add_between(33,50)
llst1.add_end(38)
llst1.delete_by_value(38)
llst1.add_end(98)
llst1.delete_by_value(98)


llst1.print__ll()