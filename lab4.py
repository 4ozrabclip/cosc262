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
####QUESTION 2
# Write a function transpose(adj_list) that takes the adjacency list of a graph and returns the adjacency list of the reverse (transpose) of the graph. 
# The returned adjacency list must follow the same format and type described in the adjacency_list question. 
# The order of elements in inner lists does not matter; all the tests in this question sort the inners list before printing them.

# For this question, the function adjacency_list is available on the server. 
# You do not have to provide your own copy of this function (however, you can if you wish so).


# def transpose(adj_list):
#         if len(adj_list) == 0:
#             return []
            
#         result = [[] for _ in range(len(adj_list))]

#         for source, neighbours in enumerate(adj_list):
#              for neighbour, w in neighbours:
#                   result[neighbour].append((source, w))

#         return result

 	

# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# graph_adj_list = adjacency_list(graph_string)
# print(graph_adj_list)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

####QUESTION 3
# Write a function is_strongly_connected(adj_list) that takes the adjacency list 
# of a graph which has at least one vertex, and returns true if the graph is strongly connected, false otherwise.

def is_strongly_connected(adj_list):
    state = [-1] * len(adj_list)
    state[adj_list[0]] = 0
    for source, neighbours in adj_list:
        if state[source] == -1:
            state[source] = 0

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

