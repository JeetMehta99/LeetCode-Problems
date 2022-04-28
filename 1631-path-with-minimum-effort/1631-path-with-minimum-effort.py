class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        output = 0
        heap = [(0, 0, 0)] # (min threshold, x, y)
        visited = set()
        while heap:
            k, x, y = heappop(heap)
            output = max(output, k)
            
            if(x,y) == (m-1, n-1): # reached to the end
                return output
            visited.add((x,y))
            for x1, y1 in dirs:
                x2, y2 = x+x1, y+y1
                if 0<= x2< m and 0<= y2< n and (x2, y2) not in visited: # check if in bounds
                    k2 = abs(heights[x][y] - heights[x2][y2])
                    heappush(heap, (k2, x2, y2))
        return -1