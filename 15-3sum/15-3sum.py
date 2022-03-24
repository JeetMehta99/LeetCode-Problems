class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print(nums)
        arr = []
        nums.sort()
        n = len(nums)
        for idx,val in enumerate(nums):
            if idx>0 and val == nums[idx-1]:
                continue
            
            l, r = idx+1, n-1
            while l<r:
                threeS = val + nums[l] + nums[r]
                if threeS > 0:
                    r -= 1
                elif threeS < 0:
                    l += 1
                else:
                    arr.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return arr
        