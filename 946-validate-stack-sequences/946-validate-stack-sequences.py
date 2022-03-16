class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack_Arr = []
        i = 0
        for val in pushed:
            stack_Arr.append(val)
            while stack_Arr and stack_Arr[-1] == popped[i]:
                stack_Arr.pop()
                i += 1
            
        return not stack_Arr
    