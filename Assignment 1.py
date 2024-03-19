################################################# QUESTION 1 #####################################################################################

from collections import deque    
def adjacency_list(converters_info):
        if len(converters_info) == 0:
            return []

        lines = converters_info.splitlines()
        list_graph_str = [e.split() for e in lines]
        vertices = int(list_graph_str[0][1])
        result = [[] for _ in range(vertices)]

        for line in list_graph_str[1:]:
            source = int(line[0])
            dest = int(line[1])

            result[source].append(dest)

        return result

def bfs_tree(adj_list, s):
        n_vertices = len(adj_list)
        state = ["undiscovered"] * n_vertices
        parent_array = [None] * n_vertices
        Q = deque()
        state[s] = "discovered"
        Q.append(s)

        while Q:
            u = Q.popleft()
            for v in adj_list[u]:
                if state[v] == "undiscovered":
                    state[v] = "discovered"
                    parent_array[v] = u
                    Q.append(v)
            state[u] = "P"

        return parent_array

def tree_path(parent, s, t):
        if s == t:
            return [s]
        elif t == None:
            return "No solution!"
        else:
            shortest_path = tree_path(parent, s, parent[t])
            if type(shortest_path) == str:
                return shortest_path
            shortest_path.append(t)
            return shortest_path

def format_sequence(converters_info, source_format, destination_format):

    adj_list = adjacency_list(converters_info)

    parent = bfs_tree(adj_list, source_format)

    shortest_path = tree_path(parent, source_format, destination_format)
    return shortest_path



############################### QUESTION 2 ########################################################################################################
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

#         return adj_list

# def bubbles(physical_contact_info):
#     adj_list = adjacency_list(physical_contact_info)

#     bubbles = len(adj_list)
#     pass

# physical_contact_info = """\
# U 2
# 0 1
# """
# print(adjacency_list(physical_contact_info))