def add_node(v):
    global node_count
    if v in nodes :
        print(v,"is already present")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,cost):
    if v1 not in nodes :
        print(v1,"not present")
    elif v2 not in nodes :
        print(v2,"not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1] [index2] = cost
        graph[index2] [index1] = cost


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format (graph[i][j],"<3"),end=" ")
        print()

nodes = []
graph = []
node_count = 0
print("before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_edge("A","B",9)
add_edge("A ","D",5)
print(graph)

print_graph()