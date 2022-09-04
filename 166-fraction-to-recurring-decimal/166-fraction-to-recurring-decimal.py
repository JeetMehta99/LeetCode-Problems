class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0 or denominator == 0: 
            return '0'
        
        result = []
        if numerator*denominator < 0:
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        result.append(str(numerator // denominator))
        
        remainder = numerator % denominator
        
        if remainder == 0: return ''.join(result)
        result.append('.')
        
        dic = {}
        while remainder != 0:
            if remainder in dic:
                result.insert(dic[remainder], '(')
                result.append(')')
                return ''.join(result)
            
            dic[remainder] = len(result)
            
            remainder *= 10
            result += str(remainder // denominator)
            remainder = remainder % denominator
        
        return ''.join(result)