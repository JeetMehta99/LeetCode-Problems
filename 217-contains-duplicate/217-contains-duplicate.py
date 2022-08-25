class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # num_dup = []
        # for i in nums:
        #     if i in num_dup:
        #         return True
        #     else:
        #         num_dup.append(i)
        # return False
        return len(nums) != len(set(nums))