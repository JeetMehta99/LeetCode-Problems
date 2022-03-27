        
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses: return []
        # build a graph
        graph = {} 
        for _to, _from in prerequisites:
            graph.setdefault(_from, []).append(_to)
            
        # topological sort by dfs
        order = deque()
        visited, visiting = set(), set() # course is already visited or present in path
        
        def dfs(node):
            # Cycle check
            if node in visiting: return False
            visiting.add(node)
            
            # explore children
            result = True
            
            for child in graph.get(node, []):
                if child not in visited: result &= dfs(child)
                # prune tree if cycle was found
                if not result: return False
            
            # add to order
            order.appendleft(node)
            # mark as visited
            visiting.discard(node)
            visited.add(node)
            return result
        
        # explore the graph
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i): return []
        return list(order)