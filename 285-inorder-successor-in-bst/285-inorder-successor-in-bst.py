# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        cur = root
        candidate = None      
        while cur:
            if cur.val > p.val:
                candidate = cur
                cur = cur.left #move left and see if even smaller val could be greater than p
            else:
                cur = cur.right 
        return candidate