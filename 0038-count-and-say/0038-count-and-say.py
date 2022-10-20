class Solution:
    def countAndSay(self, N: int) -> str:
        if N == 1:
            return '1'
        x = '1'
        for i in range(N-1):
            count = 0
            dummy_str = ''
            prevStr = x[0]
            for eachStr in x:
                if prevStr != eachStr:
                    dummy_str += str(count) + prevStr
                    prevStr = eachStr
                    count = 1
                else:
                    count += 1
            dummy_str += str(count) + prevStr
            x = dummy_str
        return x