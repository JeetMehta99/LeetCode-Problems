class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count1 = Counter(nums) # O(N) 
        for key,val in count1.items():
            if val == 1:
                return key
            
        # a = 0 # O(1)
        # for i in nums:
        #     a ^= i
        #     print(a)
        # return a
            
            