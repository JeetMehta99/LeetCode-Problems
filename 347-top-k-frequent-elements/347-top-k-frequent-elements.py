class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N) 
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # index is freq/ count; val; times it was encountered
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, cnt in count.items():
            freq[cnt].append(n) # this value n appears c number of times
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
        
        
        