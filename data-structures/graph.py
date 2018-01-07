import operator
from collections import defaultdict

class Graph(object):
    def __init__(self, adjacency_list=None, edge_list=None):
        self.graph = defaultdict(set)

        if adjacency_list:
            for node, adjacent_nodes in adjacency_list.items():
                self.graph[node] = set(adjacent_nodes)
    
        if edge_list:
            for node1, node2 in edge_list:
                self.add(node1, node2)

    def add(self, node1, node2=None):
        if node2:
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)
        else:
            self.graph[node1] = set()

    def remove(self, node):
        if node in self.graph:
            for connected_node in self.graph[node]:
                self.graph[connected_node].remove(node)
            del self.graph[node]

    def degree(self, node):
        return len(self.graph[node])

    def dfs(self, node):        
        traversed, visited, stack = list(), set(), [node]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                traversed.append(vertex)
                visited.add(vertex)
                stack.extend(self.graph[vertex] - visited)
        return traversed
    
    def bfs(self, node):
        traversed, visited, queue = list(), set(), [node]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                traversed.append(vertex)
                visited.add(vertex)
                queue.extend(self.graph[vertex] - visited)
        return traversed

    @property
    def max_degree(self):
        return max(len(connection) for connection in self.graph.values())
    
    def __str__(self):
        return '{} ({})'.format(self.__class__.__name__, dict(self.graph))


graph = Graph(edge_list=[('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')])
print(graph)
print(graph.max_degree)
    
graph.remove('B')
print(graph)

graph = Graph(adjacency_list={'A': ['B'], 'B': ['C', 'D', 'A'], 'C': ['B', 'F', 'D'], 'D': ['B', 'C'], 'E': ['F'], 'F': ['C', 'E']})
print(graph)
print(graph.dfs('B'))
print(graph.bfs('B'))