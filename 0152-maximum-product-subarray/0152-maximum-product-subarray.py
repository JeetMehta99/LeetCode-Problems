class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minPtr, maxPtr = 1, 1
        for n in nums:
            if n == 0:
                minPtr, maxPtr = 1, 1
                continue
            temp = n * maxPtr
            maxPtr = max(n*maxPtr, n*minPtr, n)
            minPtr = min(temp, n*minPtr, n)
            res = max(res, maxPtr)
        
        return res