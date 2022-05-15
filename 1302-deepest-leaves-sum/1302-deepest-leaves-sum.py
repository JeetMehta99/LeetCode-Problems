# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # BFS
        q = deque()
        q.append((root, 0))
        depth = 0 # maximum depth
        res = 0
        while q:
            node, dep = q.popleft()
            if dep > depth: 
                res = 0
                depth = dep
            if dep == depth:
                res += node.val
            
            if node.left:
                q.append((node.left, dep+1))
            
            if node.right:
                q.append((node.right, dep+1))
        return res
        