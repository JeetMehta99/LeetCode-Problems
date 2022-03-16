class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split = path.split("/")
        stack_Arr = []
        for p in path_split:
            if p in ['', '.']:
                continue
            elif p == '..':
                if stack_Arr:
                    stack_Arr.pop()
            else:
                stack_Arr.append(p)
        # print('/' + '/'.join(stack_Arr))
        return '/' + '/'.join(stack_Arr)
        