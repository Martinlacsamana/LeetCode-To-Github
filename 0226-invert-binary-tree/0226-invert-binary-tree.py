# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Strat: Regular DFS with just swapping nodes

    # Time Complexity: O(n) - We iterate throgh the nodes once.
    # Space Complexity: O(n) - We open up n frames for the recursion.

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        # Swap the right and left branches
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

      
        

            
        
        