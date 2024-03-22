#####QUESTION 2 
#write a function that converts a multiline string into an adjacency list
graph_str = """\
U 4
2 3
1 0
2 1
"""
# def adjacency_list(graph_str):
    # if len(graph_str) == 0:
    #     return []
    
    # lines = graph_str.splitlines()
    # list_graph = [e.split() for e in lines]

    # is_undirected = list_graph[0][0] == 'U'
    # is_weighted = len(list_graph[0]) == 3
    # n = int(list_graph[0][1])

    # result = [[] for _ in range(n)]

    # for line in list_graph[1:]:
    #     u = int(line[0])
    #     v = int(line[1])
    #     w = int(line[2]) if is_weighted else None

    #     result[u].append((v, w))
    #     if is_undirected:
    #         result[v].append((u, w))

    # return result

# print(adjacency_list(graph_str))

def adjacency_matrix(graph_str):
    if len(graph_str) == 0:
        return []
    
    lines = graph_str.splitlines()
    list_graph = [e.split() for e in lines]

    is_undirected = list_graph[0][0] == 'U'
    is_weighted = len(list_graph[0]) == 3
    n = int(list_graph[0][1])

    result = [[None] * n for _ in range(n)] if is_weighted else [[0] * n for _ in range(n)]
    

    result = [[] for _ in range(n)]

    for line in list_graph[1:]:
        u = int(line[0])
        v = int(line[1])
        w = int(line[2]) if is_weighted else None
        
        if is_undirected:
            result[v][u] = 1
        result[u][v] = 1

    return result

print(adjacency_matrix(graph_str))