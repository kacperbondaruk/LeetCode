# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        dummy = []
        
        def recursive(node):
            if not node:
                return
            
            recursive(node.left)
            dummy.append(node.val)
            recursive(node.right)
        
        recursive(root)
        return dummy