class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # i = 0
        # while i < len(nums1):
        #     if nums1[i] in nums2:
        #         res += [nums1[i]]
        #         nums2.remove(nums1[i])
        #     i += 1
        # return res
    
        d = Counter(nums1)
        # print(d)
        res = []
        
        for num in nums2:
            if d[num] > 0:
                d[num] -= 1
                res.append(num)
                
        return res