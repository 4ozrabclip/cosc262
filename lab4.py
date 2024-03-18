import math

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

# def dfs_tree(adj_list, start):
#     vertices = len(adj_list)
#     state = ['undiscovered'] * vertices
#     parent = [None] * vertices
#     state[start] = 0

#     topological_stack = []

#     def dfs_loop(u):
#         for v, weight in adj_list[u]:
#             if state[v] == 'undiscovered':
#                 state[v] = 'discovered'
#                 parent[v] = u
#                 dfs_loop(v)
#         topological_stack.append(u)
#         state[u] = 'processed'
#     dfs_loop(start)

#     print(state)
#     print(topological_stack)
#     return parent

# graph_string = """\
# D 5
# 0 2
# 1 2
# 2 4
# 2 3
# """

# adj_list = adjacency_list(graph_string)

# print(dfs_tree(adj_list, 0))

# def transpose(adj_list):
#         if len(adj_list) == 0:
#             return []
            
#         result = [[] for _ in range(len(adj_list))]

#         for source, neighbours in enumerate(adj_list):
#              for neighbour, w in neighbours:
#                   result[neighbour].append((source, w))

#         return result


graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

graph_adj_list = adjacency_list(graph_string)
# print(graph_adj_list)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

####QUESTION 3
# Write a function is_strongly_connected(adj_list) that takes the adjacency list 
# of a graph which has at least one vertex, and returns true if the graph is strongly connected, false otherwise.



# def is_strongly_connected(adj_list):
#      for i in range(0, len(adj_list) - 1):
#           state_1 = dfs_tree(adj_list, i)
#           if 'undiscovered' in state_1:
#                return False
#           else:
#             state_2 = dfs_tree(transpose(adj_list), i)
#             if 'undiscovered' in state_2:
#                 return False
#             return True
    

####    ####    ####    PRIMS ALGO    ####    ####     ####     ####    ####      DJIKSTRAS ALGO      ####    ####    ####      ####    ####


def next_vertex(in_tree, distance):
    closest = None
    min_value = math.inf

    for v in range(len(in_tree)):
        if not in_tree[v] and distance[v] <= min_value:
            closest = v
            min_value = distance[v]

    return closest

in_tree = [True, True, True, False, True]####test next_vertex
distance = [math.inf, 0, math.inf, math.inf, math.inf]####test next_vertex
print(next_vertex(in_tree, distance))####test next_vertex
# def prim(adj_list, s):
#     vertices = len(adj_list)
#     if vertices == 0:
#         return [], []
    
#     in_tree = [False] * vertices
#     distance = [math.inf] * vertices
#     parent = [None] * vertices
    
#     distance[s] = 0

#     while not all(in_tree):
#         u = next_vertex(in_tree, distance)
#         in_tree[u] = True
#         for v, weight in adj_list[u]:
#             if not in_tree[v] and weight < distance[v]:
#                 distance[v] = weight
#                 parent[v] = u

#     print(in_tree)

#     return parent, distance

# print(prim(graph_adj_list, 0))