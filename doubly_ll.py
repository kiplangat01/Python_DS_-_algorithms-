# class for a node 
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

# class fo doubly linkedlis
class doublyll:
    def __init__(self):
        self.head = None 
# function to print linkedlist
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.nref

# function to print ll from the last node 
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.pref

# inserting element to an empty list
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

# adding element from the begining of a list
    def add_begin(self,data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                new_node.nref = self.head
                self.head.pref = new_node
                self.head = new_node

# adding elements from the end of a list
    def add_end(self,data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                n = self.head
                while n.nref is not None:
                    n = n.nref
                n.nref = new_node
                new_node.pref = n

# adding element after a specific node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.nref
        if n is None:
            print("Given Node is not presnt in Linked List!")
        elif n.nref is None:
            new_node = Node(data)
            n.nref = new_node
            new_node.pref = n
        else:
            new_node = Node(data)
            n.nref.pref = new_node
            new_node.nref = n.nref
            n.nref = new_node
            new_node.pref = n

# adding element after a certain node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is Empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            self.head.pref = new_node
            new_node.nref = self.head
            self.head = new_node            
            return
        n = self.head
        while n.nref is not None:
            if x == n.nref.data:
                break
            n = n.nref
        if n.nref is None:
            print("Given Node is not presnt in Linked List!")
        else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node            
            n.nref = new_node

# deleting the first element in the linkedlist
    def delete_begin(self):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            self.head = self.head.nref
            self.head.pref = None

# deleting elements from the end of the list
    def delete_end(self):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

# deleting element using specified value
    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head = None
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x==n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data==x:
                n.pref.nref = None
            else:
                print("x is not present in dll!")

# calling functions
dll = doublyll()
dll.print_LL_reverse()