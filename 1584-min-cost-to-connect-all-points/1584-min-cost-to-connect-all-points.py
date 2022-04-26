# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         # Minimum Spanning tree - Prim's
#         # O(n^2logn) n : no. of points, logn : min heap(Prim's)
#         n = len(points)
#         # create an adj list
#         adj = {i:[] for i in range(n)} # each point in list is index of that point. each point i(node) is mapped to an empty list. list of [cost, node], each edge is weighted edge
        
#         for i in range(n):
#             x1, y1 = points[i] # get CoOrds
#             for j in range(i+1, n):
#                 if i == j:
#                     continue
#                 x2, y2 = points[j]
#                 dist = abs(x1-x2) + abs(y1-y2) # manhanttan distance
#                 adj[i].append([dist,j]) # append cost/dist
#                 adj[i].append([dist,i]) # undirected hence have to do both ways
#         # EO building adj list
        
#         # Prims
#         res = 0 # cost
#         visit = set() 
#         minH = [[0,0]] # cost, point
#         while len(visit) < n: 
#             cost, i = heapq.heappop(minH)
#             if i in visit:
#                 continue
#             res += cost
#             visit.add(i)
#             for nCost, nei in adj[i]:
#                 if nei not in visit: 
#                     heapq.heappush(minH, [nCost, nei])
#         return res
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = { i:[] for i in range(N) } # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]] # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res