class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                str_k = ""
                while stack[-1] != "[":
                    str_k = stack.pop() + str_k
                stack.pop()

                substr = ""
                while stack and stack[-1].isdigit():
                    substr = stack.pop() + substr
                stack.append(int(substr) * str_k)
        return "".join(stack)