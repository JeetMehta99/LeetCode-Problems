class Solution:
    def countBits(self, n: int) -> List[int]:
        # x = 6
        # x = '{0:b}'.format(x)
        # print(type(x))
        # print(x)
        arr = []
        for i in range(n+1):
            str_i = '{0:b}'.format(i)
            count = 0
            for j in range(len(str_i)):
                if str_i[j] == '1':
                    count += 1
            arr.append(count)
        return arr
                
            
        # for i in range(n):
            