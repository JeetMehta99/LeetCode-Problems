class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Union Find
        n = len(s)
        parents = [x for x in range(n)]
        
        # find group elemt belongs to
        def ufind(x):
            if parents[x] != x: 
                parents[x] = ufind(parents[x]) # if x is not root then find the root
            return parents[x]
        
        # Merges two groups together
        def uunion(a, b):
            a1 = ufind(a) # set a
            b1 = ufind(b) # set b
            parents[a1] = b1 # point childs of "set a" to root of "set b"
            
        for u, v in pairs:
            uunion(u,v)
        
        # Mapping
        eqClasses = collections.defaultdict(list)
        
        # Putting classes together and string together
        for i in range(n):
            root = ufind(i)
            eqClasses[root].append(s[i])
        
        
        for key in eqClasses.keys():
            eqClasses[key] = collections.deque(sorted(eqClasses[key]))  # helps keep track of index
            
        # Reconstruct
        res = []
        for i in range(n):
            res.append(eqClasses[ufind(i)].popleft())
                        # to get root again
        return "".join(res)
        
            