class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        q = collections.deque()
        
        inf = 10**15
        distance = [[inf] * c for _ in range(r)]
        def enqueue(x, y, d):
            distance[x][y] = d
            q.append((x, y, d))
        
        if grid[0][0] == 0:
            enqueue(0, 0, 1)
        
        directions = [(1, 0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
        while len(q) > 0:
            x, y, d = q.popleft()
            
            for dx, dy in directions:
                x1, y1 = x+dx, y+dy
                
                if 0 <= x1 < r and 0 <= y1 < c and grid[x1][y1] == 0 and distance[x1][y1] == inf:
                    enqueue(x1, y1, d+1)
        
        if distance[r-1][c-1] == inf:
            return -1
        
        return distance[r-1][c-1]