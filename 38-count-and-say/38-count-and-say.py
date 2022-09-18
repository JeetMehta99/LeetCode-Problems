class Solution:
    def countAndSay(self, N: int) -> str:
        # print(n)
        if N == 1:
            return '1'
        
        x = '1'
        for i in range(N-1):
            count = 0
            str1 = ''
            prevStr = x[0]
            for eachStr in x:
                if prevStr != eachStr:
                    str1 += str(count) + prevStr
                    prevStr = eachStr
                    count = 1
                else:
                    count += 1

            str1 += str(count)+ prevStr
            x = str1
        return x


# class Solution:
#     def get_count_say(self, num_str):
#         num_str += "*"
        
#         count = 1
#         ans_str = ''

#         for i in range(1,len(num_str)):
#             if num_str[i-1] == num_str[i]:
#                 count += 1
#             else:
#                 ans_str += str(count)+num_str[i-1]
#                 count = 1
        
#         return ans_str
                    
        
#     def countAndSay(self, n: int) -> str:        
#         if n==1:
#             return "1"
            
#         return self.get_count_say(self.countAndSay(n-1))

#     lass Solution:
#     def get_count_say(self, num_str):
#             i = 0
#             up_str = ""
#             while i<len(num_str):
#                 curr_char = num_str[i]
#                 j = i
#                 while j<len(num_str) and num_str[j] == curr_char:
#                     j += 1
#                 freq = j-i
#                 up_str += str(freq)+curr_char
#                 i = j
#             return up_str
        
#     def countAndSay(self, n: int) -> str:        
#         if n==1:
#             return "1"
            
#         return self.get_count_say(self.countAndSay(n-1))

#         def freq(numString):
#             n = len(numString)
            
#             # if numString == '1':
#             #     return '11'
#             # firstStr = numString[0]
#             count = 1
#             # for_given_str = 0
#             arr = []
#             arr1 = []
#             for i in range(n-1,-1,-1):
#                 # dummy_str = ''
#                 # print("Here")
#                 if numString[i] == numString[i-1]:
#                     count += 1 
#                     # for_given_str = numString[i] 
#                 elif i == 0:
#                     arr.append(count)
#                     arr1.append(numString[i])
#                     count = 1
                    
#                 else:
#                     arr.append(count)
#                     arr1.append(numString[i])
#                     count = 1
#             revCount = list(reversed(arr))
#             revDigit = list(reversed(arr1))
#             # print(revCount)
#             # print(revDigit)
#             n = len(revCount)
#             # print(n)
#             dummyStr = ''
#             for i in range(n):
#                 dummyStr += str(revCount[i]) + revDigit[i]
#                 print(dummyStr)
#             return dummyStr
#         numString = "3333"
#         print(freq(numString))
#         x = '1'
#         for k in range(1, N):
#             x = freq(x)
            
#             # print(z)
#         return x

                