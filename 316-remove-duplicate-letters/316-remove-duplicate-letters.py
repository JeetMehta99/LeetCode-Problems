class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
#         dic = {}
#         for i in range(len(s)):
#             dic[s[i]] = i
            
#         stack_Arr = []
#         visited = set()
#         for i in range(len(s)):
#             if s[i] in visited:
#                 continue
#             while stack_Arr and s[i] < stack_Arr[-1] and dic[stack_Arr[-1]] > i:
#                 visited.remove(stack_Arr[-1])
#                 stack_Arr.pop()
                
#             stack_Arr.append(s[i])
#             visited.add(s[i])
#         return "".join(stack_Arr)
        
        arr = []
    
        for i in range(len(s)):
            if s[i] in arr:
                continue

            while arr and s[i] < arr[-1] and arr[-1] in s[i+1:]:
                arr.pop()

            arr.append(s[i])
        
        return "".join(arr)
                
        
#         visited = set()
#         s = list(s)
#         temp = ""
#         for i in s:
#             if i not in visited:
#                 temp += i
#                 visited.add(i)
            
#         return ''.join(sorted(visited))
        