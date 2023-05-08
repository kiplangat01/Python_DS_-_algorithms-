nodes = []
node_count = 0
graph = []


def add_node(v):
    global nodes,node_count,graph
    if v in graph:
        print(v,"already present`")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edge(v1,v2,e):
    global graph
    if v1 not in graph:
        print("absent in graph")
    elif v2 not in graph:
        print("absent in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = e
        graph[index2][index1] = e


def delete_node(v):
    if v not in nodes:
        print(v,"not present")
    else:
        index1 = nodes.index(v)
        node_count = node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3",end=" "))
        print()



add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",10)
delete_node("A")
print(graph)