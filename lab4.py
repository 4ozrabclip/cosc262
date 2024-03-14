####QUESTION 2
# Write a function transpose(adj_list) that takes the adjacency list of a graph and returns the adjacency list of the reverse (transpose) of the graph. 
# The returned adjacency list must follow the same format and type described in the adjacency_list question. 
# The order of elements in inner lists does not matter; all the tests in this question sort the inners list before printing them.

# For this question, the function adjacency_list is available on the server. 
# You do not have to provide your own copy of this function (however, you can if you wish so).
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

def transpose(adj_list):
     pass

graph_string = """\
D 3
0 1
1 0
0 2
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))