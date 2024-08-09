# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Strat: DFS that returns depth of each subtree, flagging if unbalanced
    # Time Complexity: O(N)
    # Space Complexity: O(N)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        # DFS to get depth
        def dfs(node):
            nonlocal balanced
            if not node: 
                return 0

            left, right = dfs(node.left), dfs(node.right)

            # Flag if we the branches difference is more than 2
            if abs(left - right) >= 2:
                balanced = False
            
            # Expected return statement for capturing max depth in dfs
            return max(left, right) + 1

        dfs(root)
        return balanced
        


           

        
        