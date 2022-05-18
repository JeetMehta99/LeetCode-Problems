class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dist = [0] * n
        low = [0] * n
        self.time = 0
        visited = set()
        res = []
        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(cur, prev):
            visited.add(cur)
            self.time += 1
            dist[cur] = low[cur] = self.time
            
            for next in graph[cur]:
                if next not in visited:
                    dfs(next, cur)
                    low[cur] = min(low[cur], low[next])
                    
                elif next != prev:
                    low[cur] = min(low[cur], dist[next])
                
                if low[next] > dist[cur]:
                    res.append([cur, next])
        dfs(0, -1)
        
        return res