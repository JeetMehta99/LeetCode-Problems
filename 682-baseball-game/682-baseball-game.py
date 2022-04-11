class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        # add = 0
        for i in ops:
            if i == "C":
                arr.pop()
            elif i == "D":
                arr.append(arr[-1]*2)
            elif i == "+":
                arr.append(arr[-1]+arr[-2])
            else:
                arr.append(int(i))
        # for i in output:
        #     add += i
        return sum(arr)
        