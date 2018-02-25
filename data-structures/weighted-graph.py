import operator
from heapq import *
from collections import defaultdict

class WeightedGraph(object):
    def __init__(self, weighted_edge_list=None):
        self.graph = defaultdict(set)
        self.weights = defaultdict(int)

        if weighted_edge_list:
            for node1, node2, weight in weighted_edge_list:
                self.add(node1, node2, weight)

    def add(self, node1, node2, weight):
        self.graph[node1].add(node2)
        self.graph[node2].add(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight
    
    def dijkstras(self, from_node):
        queue, visited, shortest = list(), set(), defaultdict(lambda: float('inf'))
        queue.append((0, from_node))
        
        while queue:
            cost, node = heappop(queue)
            if node not in visited:
                visited.add(node)
                shortest[node] = min(shortest[node], cost)
                for neighbor in self.graph[node]:
                    heappush(queue, (cost + self.weights[(node, neighbor)]))
        
        return shortest

    
    def __str__(self):
        return '{} ({})'.format(self.__class__.__name__, dict(self.graph))


graph = WeightedGraph(weighted_edge_list=[
    ('A', 'B', 6),
    ('A', 'D', 1),
    ('D', 'B', 2),
    ('D', 'E', 1),
    ('B', 'E', 2),
    ('B', 'C', 5),
    ('E', 'C', 5),
])
print(graph)
print(graph.dijkstras('A'))