# creating node 
from itertools import count


class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
           self.key = data
           return
        if self.key == data:
            return
        if self.key > data :
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self,data):
        if self.key == data:
            print("node found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node absent")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node absent")

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
            
    def postorder(self):
            if self.lchild:
                self.lchild.postorder()
            if self.rchild:
                self.rchild.postorder()
            print(self.key,end=" ")

    def delete(self,data,curr):
        if self.key is None:
            print("empty tree")
            return
        if data < self.key :
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                 print("given node ablsent in the tree")
        elif data > self.key :
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("given node absent in the tree")
        else:
            if self.lchild is None :
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return temp
            if self.rchild is None :
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return 
                
        node = self.rchild
        while node.lchild:
            node = node.lchild
        self.key = node.key
        self.rchild = self.rchild.delete(node.key,curr)

    def count(node):
        if node is None:
            return 0
        return 1+count(node.lchild)+count(node.rchild)
    
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("min node is:",current.key)
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("max node is:",current.key)

root = BST(10)
list1 = [6,3,1,6,98,3,7,100]
for i in list1:
    root.insert(i)
print("preorder")
root.preorder()
print()

root.min_node()
root.max_node()