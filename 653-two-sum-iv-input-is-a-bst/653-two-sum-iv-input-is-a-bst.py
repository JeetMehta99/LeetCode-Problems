# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dic = {}
        val = []
        
        def getVal(root, depth):
            if not root:
                return
				
            val.append(root.val)  # for each move, store the value

            getVal(root.left, depth+1)
            getVal(root.right, depth+1)
        
        getVal(root, 1)  # start from the top of the BST
        
        # Simple 2 Sum problem
        for i in range(len(val)):
            complement = k - val[i]
            if complement in dic:
                return True
            dic[val[i]] = i
            
        return False