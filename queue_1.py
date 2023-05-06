my_queue = []

# adding items in the queue
def enqueue():
    e = input("enter element")
    my_queue.append(e)
    print(e, "added")

# removing items in the queue
def dequeue():
    if not my_queue:
        print("empty queue")
    else:
        e = my_queue.pop(0)
        print("removed" ,e)

# diplay queue
def show():
    print(my_queue)


# input choices 
while True:
    print("select the option 1.add 2.remove 3.show 4.quit")
    option = int(input())

    if option==1:
       enqueue()

    if option==2:
       dequeue()

    if option==3:
       show()
    elif option==4:
        break
    # 