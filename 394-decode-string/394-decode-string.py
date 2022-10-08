class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                str_dummy = ""
                while stack[-1] != "[":
                    str_dummy = stack.pop() + str_dummy
                stack.pop()
                str_dummy1 = ""
                while stack and stack[-1].isdigit():
                    str_dummy1 = stack.pop() + str_dummy1
                stack.append(int(str_dummy1)*str_dummy)
        return "".join(stack)