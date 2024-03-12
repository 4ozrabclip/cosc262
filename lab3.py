from pprint import pprint
####QUESTION 2
# Write a function adjacency_list(graph_str) that takes the textual representation of a graph (as a string) and returns its adjacency list.

# The returned adjacency list must be a list of lists. The length of the outer list is equal to the number of vertices. 
# The inner lists have one element for each edge. The elements are two-tuples where the first element of the tuple is the vertex the edge goes to, 
# and the second element of the tuple is the weight. For unweighted graphs the second element of the tuple is None. 
# The inner lists must be populated as the edge information is read from the graph string. This order is important. 
# Note that for undirected graphs, each edge is stored two times (in opposite directions).

# Note: In some programming questions in future quizzes you have to include the definition of the adjacency_list function.

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

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
print(adjacency_list(graph_string))

####QUESTION 3
# Write a function adjacency_matrix(graph_str) that takes the textual representation of a graph (as a string) and returns its corresponding adjacency matrix.

# The returned adjacency matrix must be a list of lists. 
# The length of the outer list and the length of all the inner lists are equal to the number of vertices. 
# For unweighted graphs the returned matrix should only include numbers 0 or 1. 
# For weighed graphs, use None when there is no edge and numbers for weights.

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


# graph_string = """\
# U 17
# 1 2
# 1 15
# 1 6
# 12 13
# 2 15
# 13 4
# 4 5
# """

# pprint(adjacency_matrix(graph_string))

####QUESTION 12
# Write a function bfs_tree(adj_list, start) that takes an adjacency list and a starting vertex (an integer), 
# performs a breadth-first search and returns the parent array at the end of the search.

# The elements of the parent array must be initialised to None at the beginning of the search.

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

####QUESTION 13
# Write a function dfs_tree(adj_list, start) that takes an adjacency list and a starting vertex (an integer), 
# performs a depth-first search and returns the parent array at the end of the search.

# The parent array must be initialised to None at the beginning of the search.

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