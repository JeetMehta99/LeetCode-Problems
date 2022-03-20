class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        m = len(bottoms)
        dictA= defaultdict(int)
        dictB = defaultdict(int)
        same = 0

        for i in range(n):
            dictA[tops[i]] += 1
            dictB[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same += 1
    
        for x in range(1,7):
            if (dictA[x] + dictB[x] - same) == n:
                return n - max(dictA[x], dictB[x])

        return -1
