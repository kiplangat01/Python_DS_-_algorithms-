import collections
import queue

# creating stack
my_stack = []


# adding elements to the stack
my_stack.append(10)


# removing element from stack
my_stack.pop()

my_stack.pop()

print(my_stack)
# cheking the length of the stack
len(my_stack)

# checking the last element of the stack
my_stack[-1]

# creating stack and enable user to input elements
stack = []

# function to add elements to stack
def push():
    element = input("input element")
    stack.append(element)
    print(element)

# function to add elements to the stack
def pop_element():
    if not stack:
        print("empty stack please input element")

    else:
        e = stack.pop()
        print("removed element:", e)
        print(stack)


# conditions and choices
while True:
    print("select the operation 1. push 2. pop 3. quit")
    choice = int(input())
    if choice==1:
       push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("incorrect choice")


# iplement using module

new_stack = collections.deque()

# adding
new_stack.append(14)
new_stack.append(13)
new_stack.append(16)
new_stack.append(46)

# removing
new_stack.pop()
new_stack.pop()
new_stack.pop()


queue_stack = queue.LifoQueue()


queue_stack.put(9)

queue_stack.put(4)

queue_stack.put(5)

stack