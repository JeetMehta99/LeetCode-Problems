class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int(low + (high-low)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1
        
        """
        [-1, 0, 3, 5, 9, 12]
        find index of 9
        
        pass 1:
        mid = 2
        is 3 == 9? no
        is 3>9? No
        low = 3
        
        pass2:
        mid = 4
        is 9 == 9? yes
        """
        