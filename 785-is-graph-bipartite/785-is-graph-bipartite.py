class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        c = [-1] * n
        for i in range(n): 
        # BFS
            if c[i] != -1:
                continue
            q = deque()
            q.append((i,0)) # 0 is first color and 1 next
            while q:
                node, colour = q.popleft()
                if c [node] == -1:
                    c[node] = colour
                    for nei in graph[node]:
                        q.append((nei, colour^1)) # exor 
                if c[node]!= colour:
                    return False
        return True
    
         