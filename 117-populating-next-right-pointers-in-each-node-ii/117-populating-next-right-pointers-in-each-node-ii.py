"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = collections.deque() # bfs
        if root is not None:
            q.append((root,0))
 
        
        while len(q) > 0:
            node, curLevel = q.popleft()
            if len(q) > 0:
                nxt, nxtNodeLevel = q[0]
                
                if curLevel == nxtNodeLevel:
                    node.next = nxt
            for nxt in [node.left, node.right]:
                if nxt is not None:
                    q.append((nxt, curLevel+1))
        return root