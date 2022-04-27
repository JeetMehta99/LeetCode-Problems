class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Union Find
        n = len(s)
        parents = [x for x in range(n)]
        
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]
        
        def uunion(a, b):
            a1 = ufind(a)
            b1 = ufind(b)
            parents[a1] = b1
            
        for u, v in pairs:
            uunion(u,v)
        
        eqClasses = collections.defaultdict(list)
        
        for i in range(n):
            root = ufind(i)
            eqClasses[root].append(s[i])
        
        for key in eqClasses.keys():
            eqClasses[key] = collections.deque(sorted(eqClasses[key]))
            
        res = []
        for i in range(n):
            res.append(eqClasses[ufind(i)].popleft())
            
        return "".join(res)
        
            