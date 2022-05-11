class Solution:
    def countVowelStrings(self, n: int) -> int:
        ## https://www.mathsisfun.com/combinatorics/combinations-permutations.html
        return factorial(n+4)// factorial(n)// 24

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ######### HORRIBLE TIME COMPLEXITY ##############
        
        #         def recursion(n, k): # k: what val we are at inside of our string
#             if n == 0:
#                 return 1
            
#             cnt = 0
#             for i in range(k, 5):
#                 cnt += recursion(n-1, i) # avoid doing anything from before coz lexicography
                
#             return cnt
#         return recursion(n, 0)