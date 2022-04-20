# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        temp = []
        def dfs(node): # does the inorder traversal 
            if not node:
                return 
            dfs(node.left)
            temp.append(node.val) # helps to get inorder
            dfs(node.right) 
            
        dfs(root)
        
        # Create a new tree
        tree = TreeNode(val=temp[0])
		# Dummy to store pointer
        tmp = tree
		# Iterate through our vals, creating a new right node with the current val.
        for i in temp[1:]:
            tmp.right = TreeNode(val=i)
			# Move the sentinel to the next node.
            tmp = tmp.right
            
        return tree