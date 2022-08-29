class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        curMaxSum = nums[0]
        for i in range(1, n):
            curMaxSum = max(curMaxSum + nums[i], nums[i])
            maxSum = max(maxSum, curMaxSum)
        return maxSum
    