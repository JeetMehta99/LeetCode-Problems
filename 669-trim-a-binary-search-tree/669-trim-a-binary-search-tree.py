# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val>high: # delete all right nodes
            return self.trimBST(root.left, low, high)
        if root.val<low: # delete all left and return right nodes
            return self.trimBST(root.right, low, high)
        
        # if root value is included in root value, but update left and right subtree of tree
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root