# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            
            # Each branch will return a node or None if not p or q
            left = dfs(node.left)
            right = dfs(node.right)

            if (left and right) or node.val == q.val or node.val == p.val:
                return node
            
            # As a way to propogate p or q up the tree if found
            return left or right
            

        lca = dfs(root)
        return lca
        