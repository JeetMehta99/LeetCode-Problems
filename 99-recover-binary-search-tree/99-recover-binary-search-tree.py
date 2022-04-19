# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.temp = []
        def dfs(node): # does the inorder traversal 
            if not node:
                return 
            dfs(node.left)
            self.temp.append(node) # helps to get inorder
            dfs(node.right)
        dfs(root)
        
        sort = sorted(n.val for n in self.temp) # sort by vals
        for i in range(len(sort)):
            self.temp[i].val = sort[i]