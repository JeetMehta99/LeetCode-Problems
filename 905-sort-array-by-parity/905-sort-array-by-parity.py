class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = []
        arr1 = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                arr.append(nums[i])
            else:
                arr1.append(nums[i])
        return arr+arr1