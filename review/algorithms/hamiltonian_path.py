

# SEE: https://stackoverflow.com/questions/47982604/hamiltonian-path-using-python

def hamiltonian(graph, start_v):
    size = len(graph)
    to_visit = [None, start_v]        # if None we are -unvisiting- comming back and pop v
    path = []
    visited = set([])
    while to_visit:
        v = to_visit.pop()
        if v:
            path.append(v)
            if len(path) == size:
                break
            visited.add(v)
            for x in graph[v]-visited:
                to_visit.append(None)       # out
                to_visit.append(x)          # in
        else:                           # if None we are comming back and pop v
            visited.remove(path.pop())
    return path
