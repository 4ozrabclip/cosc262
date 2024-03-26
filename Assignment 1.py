import math
################################################# QUESTION 1 #####################################################################################

# from collections import deque    
# def adjacency_list(converters_info):
#         if len(converters_info) == 0:
#             return []

#         lines = converters_info.splitlines()
#         list_graph_str = [e.split() for e in lines]
#         vertices = int(list_graph_str[0][1])
#         result = [[] for _ in range(vertices)]

#         for line in list_graph_str[1:]:
#             source = int(line[0])
#             dest = int(line[1])

#             result[source].append(dest)

#         return result

# def bfs_tree(adj_list, s):
#         n_vertices = len(adj_list)
#         state = ["undiscovered"] * n_vertices
#         parent_array = [None] * n_vertices
#         Q = deque()
#         state[s] = "discovered"
#         Q.append(s)

#         while Q:
#             u = Q.popleft()
#             for v in adj_list[u]: #no weight for this reference to later questions
#                 if state[v] == "undiscovered":
#                     state[v] = "discovered"
#                     parent_array[v] = u
#                     Q.append(v)
#             state[u] = "P"

#         return parent_array

# def tree_path(parent, s, t):
#         if s == t:
#             return [s]
#         elif t == None:
#             return "No solution!"
#         else:
#             shortest_path = tree_path(parent, s, parent[t])
#             if type(shortest_path) == str:
#                 return shortest_path
#             shortest_path.append(t)
#             return shortest_path

# def format_sequence(converters_info, source_format, destination_format):

#     adj_list = adjacency_list(converters_info)

#     parent = bfs_tree(adj_list, source_format)

#     shortest_path = tree_path(parent, source_format, destination_format)
#     return shortest_path



############################### QUESTION 2 ########################################################################################################
# from collections import deque
# def adjacency_list(data):
#         if len(data) == 0:
#             return []

#         lines = data.splitlines()
#         list_graph_str = [e.split() for e in lines]
#         vertices = int(list_graph_str[0][1])
#         adj_list = [[] for _ in range(vertices)]

#         for line in list_graph_str[1:]:
#             source = int(line[0])
#             dest = int(line[1])
#             adj_list[source].append(dest)
#             adj_list[dest].append((source))  ## undirected 

#         return adj_list

# def bfs_loop(adj_list, Q, state):
#     while Q:
#         u = Q.popleft()
#         for v in adj_list[u]:
#             if state[v] == "undiscovered":
#                 state[v] = "discovered"
#                 Q.append(v)

# def bubbles(physical_contact_info):
#     adj_list = adjacency_list(physical_contact_info)
#     n = len(adj_list)
#     state = ['undiscovered'] * n
#     Q = deque()
#     components = []

#     for i in range(n):
#         if state[i] == 'undiscovered':
#             prevstate = state.copy()
#             state[i] = 'discovered'
#             Q.append(i)
#             bfs_loop(adj_list, Q, state)
#             new_component = [u for u in range(n) if state[u] != prevstate[u]]
#             components.append(new_component)
#     return components



# physical_contact_info = """\
# U 7
# 1 4
# 2 0
# 4 6
# 5 3
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

########################################## QUESTION 3 #############################################################################################

# def adjacency_list(data):
#         if len(data) == 0:
#             return []

#         lines = data.splitlines()
#         list_graph_str = [e.split() for e in lines]
#         vertices = int(list_graph_str[0][1])
#         adj_list = [[] for _ in range(vertices)]

#         for line in list_graph_str[1:]:
#             source = int(line[0])
#             dest = int(line[1])
#             adj_list[source].append(dest)
#             # adj_list[dest].append((source))   # use this if its undirected

#         return adj_list


# def topological_sort(adj_list, start):
#     vertices = len(adj_list)
#     parent = [None] * vertices
#     state = ['unvisited'] * vertices
#     state[start] = 'visited'

#     topological_stack = []

#     def dfs_loop(u):
#         for v in adj_list[u]:
#             if state[v] == 'unvisited':
#                 state[v] = 'visited'
#                 parent[v] = u
#                 dfs_loop(v)
#         state[u] = 'processed'
#         topological_stack.append(u)
    
#     for v in range(len(adj_list)):
#         if state[v] != 'processed':
#             dfs_loop(v)

#     return topological_stack


# def build_order(dependencies):
        
#     adj_list = adjacency_list(dependencies)
#     dfs = topological_sort(adj_list, 0)[::-1]    ###  dependencies seems like it would be LIFO / dfs

#     return dfs

############################### QUESTION 4 ########################################################################################################
def adjacency_list(graph_str):
    if len(graph_str) == 0:
        return []
    
    lines = graph_str.splitlines()
    list_graph = [e.split() for e in lines]

    n = int(list_graph[0][1])

    result = [[] for _ in range(n)]

    for line in list_graph[1:]:
        u = int(line[0])
        v = int(line[1])
        w = int(line[2]) 

        result[u].append((v, w))
        result[v].append((u, w)) #undirected

    return result

def next_vertex(in_tree, distance):
    closest = None
    def_value = math.inf

    for v in range(len(in_tree)):
        if not in_tree[v] and distance[v] <= def_value:
            closest = v
            def_value = distance[v]

    return closest


def which_segments(city_map, start=0):
    adj_list = adjacency_list(city_map)
    
    n = len(adj_list)
    in_tree = [False] * n
    d = [math.inf] * n
    parent = [None] * n
    
    d[start] = 0

    result = []

    while not all(in_tree):
        u = next_vertex(in_tree, d)
        in_tree[u] = True
        for v, w in adj_list[u]:
            if not in_tree[v] and d[v] > w:
                d[v] = w 
                parent[v] = u
    used_array = []

    for i in range(n):
        if parent[i] is not None:
            if parent[i] < i:
                result.append((parent[i], i))
            else:
                result.append((i, parent[i]))
            # used_array.append(parent[i])
    return result


 	

city_map = """\
U 4 W
0 1 5
1 3 5
3 2 3
2 0 5
0 3 2
1 2 1
"""

print(which_segments(city_map))