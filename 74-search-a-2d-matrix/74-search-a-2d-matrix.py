class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        top, bottom = 0, rows - 1
        while top <= bottom: # Kinda like doing binary search
            row = (top + bottom)//2  # finding mid(BS)
            if target > matrix[row][-1]: # Run loop once to spot which half target number lies in
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
                
        if not (top <= bottom): # top crosses bottom thus the element doesn't exist in the matrix
            return False
        
        row = (top + bottom) // 2
        l, r = 0, cols - 1
        while l <= r:
            max = (l + r) // 2
            if target > matrix[row][max]:
                l = max + 1
            elif target < matrix[row][max]:
                r = max - 1
            else:
                return True
        return False