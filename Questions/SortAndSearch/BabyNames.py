"""
    BABY NAMES

    Each year, the government releases a list of the 10000 most common baby names and their frequencies (the number of
    babies with that name).  The only problem with this is that some names have multiple spellings.  For example, "John"
    and "Jon" are essentially the same name but would be listed separately in the list.  Given two lists, one of
    names/frequencies and the other of pairs of equivalent names, write an algorithm to print a new list of the true
    frequency of each name.  Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and
    Johnny are synonyms.  (It is both transitive and symmetric.)  In the final list, any name can be used as the "real"
    name.

    Example:
        Input   names = {"John": 15, "Jon": 12, "Chris": 13, "Kris": 4, "Christopher": 19}
                synonyms = [("Jon", "John"), ("John", "Johnny"), ("Chris", "Kris"), ("Chris", "Christopher")]
        Output  {"John":27, "Kris":36}
"""
from DataStructures.Graph import Graph


# Approach 1: Naively use list of sets.
def true_name_frequency_naive(names, synonyms):
    name_set_list = []
    for t1, t2 in synonyms:
        has_set_flag = False
        for s in name_set_list:
            if t1 in s:
                s.add(t2)
                has_set_flag = True
            elif t2 in s:
                s.add(t1)
                has_set_flag = True
        if not has_set_flag:
            name_set_list.append(set({t1, t2}))
    result = {}
    for s in name_set_list:
        count = 0
        name = None
        for n in s:
            name = n
            if n in names:
                count += names[n]
        result[name] = count
    return result


# Approach 2: Optimal--Convert names into graph, connect synonyms, then traverse once; runtime of O(B + P), where B is
# the number of baby names and P is the number of pairs of synonyms.
def true_name_frequency(names, synonyms):
    graph = construct_graph(names)
    connect_edges(graph, synonyms)
    return true_name_frequency_from_graph(graph)


def construct_graph(names):
    graph = Graph()
    for name in names.keys():
        graph.create_node(name, names[name])
    return graph


def connect_edges(graph, synonyms):
    for name_one, name_two in synonyms:
        graph.add_edge(name_one, name_two)


def true_name_frequency_from_graph(graph):
    root_names = dict()
    for node in graph.get_nodes():
        if not node.is_visited():
            root_names[node.get_name()] = get_compound_frequency(node)
    return root_names


def get_compound_frequency(node):
    if node.is_visited():
        return 0
    node.set_visited()
    sum = node.get_value()
    for neighbor in node.get_neighbors():
        sum += get_compound_frequency(neighbor)
    return sum


names = {"John": 15, "Jon": 12, "Chris": 13, "Kris": 4, "Christopher": 19}
synonyms = [("Jon", "John"), ("John", "Johnny"), ("Chris", "Kris"), ("Chris", "Christopher")]
print("names:", names)
print("synonyms:", synonyms)
print()

print("true_name_frequency_naive(names, synonyms)", true_name_frequency_naive(names, synonyms))
print()

print("true_name_frequency(names, synonyms):", true_name_frequency(names, synonyms))



