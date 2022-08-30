class Solution:
    def getSum(self, a: int, b: int) -> int:
        
#         while (b != 0):
     
#             # carry now contains common
#             carry = a & b

#             # Sum of bits of a and b where at
#             # least one of the bits is not set
#             a = a ^ b

#             # Carry is shifted by one so that  
#             # adding it to a gives the required sum
#             b = carry << 1
     
#         return a

# need to learn the concept of masks coz python works differently
# https://leetcode.com/problems/sum-of-two-integers/discuss/489210/Read-this-if-you-want-to-learn-about-masks
    # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a