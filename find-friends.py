def check_connection(network, first, second):
    
    graph = {}
    for conn in network:
        k, v = conn.split('-')
        if k in graph:
            graph[k].append(v)
        else:
            graph[k] = [v]
        if v in graph:
            graph[v].append(k)
        else:
            graph[v] = [k]

    return True if find_path(graph, first, second) else False 

def find_path(graph, start, end, path=[]):
        """
        Find a path between two nodes in a graph.
        Implementation from https://www.python.org/doc/essays/graphs/
    
        Returns path: a list of nodes
        """
        
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
