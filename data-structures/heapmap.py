'''
Map + Heap Data Structure Used for Graph Algos
'''
import heapq

class HeapMap(object):
    def __init__(self):
        self.map = dict()
        self.heap = list()
    
    def insert(self, item):
        heapq.heappush(self.heap)
        
    def extract_min(self):
        return heapq.heappop()
    
    def contains(self, item):
        return item in self.map
    
    def decrease(self, item):
        