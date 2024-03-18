def format_sequence(converters_info, source_format, destination_format):
    
    def adjacency_list():
        if len(converters_info) == 0:
            return []
        lines = converters_info.splitlines()
        list_graph_str = [e.split() for e in lines]

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
    
    adj_list = adjacency_list()

    