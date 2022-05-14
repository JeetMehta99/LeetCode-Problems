class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency list
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set() # to avoid cycle
        res = 0
        while minHeap:
            w1, frontierNode = heapq.heappop(minHeap)
            if frontierNode in visit:
                continue
            visit.add(frontierNode)
            
            res = max(res, w1)
            for nodenext, w2 in edges[frontierNode]:
                if nodenext not in visit:
                    heapq.heappush(minHeap, (w1+w2, nodenext))
        
        return res if len(visit) == n else -1
        