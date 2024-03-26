from collections import deque
def adjacency_list(data):
        if len(data) == 0:
            return []

        lines = data.splitlines()
        list_graph_str = [e.split() for e in lines]
        vertices = int(list_graph_str[0][1])
        adj_list = [[] for _ in range(vertices)]

        for line in list_graph_str[1:]:
            source = int(line[0])
            dest = int(line[1])
            adj_list[source].append(dest)
            adj_list[dest].append((source))

        return adj_list


def bfs_tree(adj, s):
     n = len(adj)
     state = ['undiscovered'] * n
     parent = [None] * n
     Q = deque()
     state[s] = 'discovered'
     Q.append(s)
     return bfs_loop(adj, Q, state, parent)

def bfs_loop(adj, Q, state, parent):
     while Q:
          u = Q.popleft()
          for v, w in adj[u]:
               if state[v] == 'undiscovered':
                    state[v] = 'discovered'
                    parent[v] = u
                    Q.append(v)
          state[u] = 'processed'
     return parent


adj = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

print(bfs_tree(adj, 0))
print(bfs_tree(adj, 1))