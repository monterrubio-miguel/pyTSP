from collections import defaultdict

class Graph:
    graph_dict = defaultdict(list)

    def add_edge(self, node, neighbour):
        self.graph_dict[node].append(neighbour)

graph = Graph()
graph.add_edge('start', ('a', 7))
graph.add_edge('start', ('b', 2))
graph.add_edge('start', ('c', 3))
graph.add_edge('a', ('start', 7))
graph.add_edge('a', ('b', 3))
graph.add_edge('a', ('d', 4))
graph.add_edge('b', ('start', 2))
graph.add_edge('b', ('d', 4))
graph.add_edge('b', ('g', 1))
graph.add_edge('b', ('a', 3))
graph.add_edge('c', ('start', 3))
graph.add_edge('c', ('k', 2))
graph.add_edge('d', ('a', 4))
graph.add_edge('d', ('b', 4))
graph.add_edge('d', ('e', 5))
graph.add_edge('e', ('d', 5))
graph.add_edge('e', ('g', 3))
graph.add_edge('f', ('g', 2))
graph.add_edge('f', ('end', 2))
graph.add_edge('g', ('b', 1))
graph.add_edge('g', ('e', 3))
graph.add_edge('g', ('f', 2))
graph.add_edge('h', ('k', 4))
graph.add_edge('h', ('i', 6))
graph.add_edge('h', ('j', 4))
graph.add_edge('i', ('k', 4))
graph.add_edge('i', ('h', 6))
graph.add_edge('i', ('j', 4))
graph.add_edge('j', ('h', 4))
graph.add_edge('j', ('i', 4))
graph.add_edge('j', ('end', 5))
graph.add_edge('k', ('c', 2))
graph.add_edge('k', ('h', 4))
graph.add_edge('k', ('i', 4))
graph.add_edge('end', ('f', 2))
graph.add_edge('end', ('j', 5))

# print(graph.graph_dict)