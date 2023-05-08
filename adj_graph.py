nodes = []
node_count = 0
graph = []
def add_node(v):
    if v in graph:
        print(v,"already present`")
    else:
        graph[v] = []

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"absent in graph")
    elif v2 not in graph:
        print(v2,"absent in graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


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




add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
print(graph)