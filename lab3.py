
graph_string = """\
U 4
0 1
0 2
0 3
1 2
1 3
"""
def adjacency_list(graph_str):

    if len(graph_str) == 0:
        return []
    lines = graph_str.splitlines()
    list_graph_str = [e.split() for e in lines]

    #directed = list_graph_str[0][0] == 'D'
    undirected = list_graph_str[0][0] == 'U'
    weighted = len(list_graph_str[0]) == 3
    vertices = int(list_graph_str[0][1])

    result = [[] for _ in range(vertices)]

    
    for line in list_graph_str[1:]:
        source = int(line[0])
        b = int(line[1])
        w = int(line[2]) if weighted else None

        result[source].append((b, w))
        if undirected:
            result[b].append((source, w))
        
            
    return result
# def adjacency_matrix(graph_str):

#     if len(graph_str) == 0:
#         return []
#     lines = graph_str.splitlines()
#     list_graph_str = [e.split() for e in lines]

#     #directed = list_graph_str[0][0] == 'D'
#     undirected = list_graph_str[0][0] == 'U'
#     weighted = len(list_graph_str[0]) == 3
#     vertices = int(list_graph_str[0][1])

#     unweighted_matrix = [[0] * vertices for _ in range(vertices)]
#     weighted_matrix = [[None] * vertices for _ in range(vertices)]
    
#     for line in list_graph_str[1:]:
#         source = int(line[0])
#         b = int(line[1])
#         w = int(line[2]) if weighted else None
#         if weighted:
#             weighted_matrix[source][b] = w
#             if undirected:
#                 weighted_matrix[b][source] = w
#         if undirected:
#             unweighted_matrix[b][source] = 1
#         unweighted_matrix[source][b] = 1 


#     if weighted:
#         return weighted_matrix
#     return unweighted_matrix

    

# print(adjacency_matrix(graph_string))
from collections import deque


def bfs_tree(adj_list, start):
    n_vertices = len(adj_list)
    state = ["undiscovered"] * n_vertices
    parent_array = [None] * n_vertices
    Q = deque()
    state[start] = "discovered"
    Q.append(start)

    while Q:
        u = Q.popleft()
        for v, w in adj_list[u]:
            if state[v] == "undiscovered":
                state[v] = "discovered"
                parent_array[v] = u
                Q.append(v)
        state[u] = "P"
        print(Q)
        print(parent_array)
        print(state)

    return parent_array



print(bfs_tree(adjacency_list(graph_string), 3))

# def dfs_tree(adj_list, start):
#     vertices = len(adj_list)
#     state = [-1] * vertices
#     parent = [None] * vertices
#     state[start] = 0

#     def dfs_loop(u):
#         for v, weight in adj_list[u]:
#             if state[v] == -1:
#                 state[v] = 0
#                 parent[v] = u
#                 dfs_loop(v)
#         state[u] = 1
#     dfs_loop(start)
#     return parent


# adj_list = [
#     [(1, None), (2, None)],
#     [(0, None), (2, None)],
#     [(0, None), (1, None)]
# ]

# print(dfs_tree(adj_list, 0))
# print(dfs_tree(adj_list, 1))
# print(dfs_tree(adj_list, 2))