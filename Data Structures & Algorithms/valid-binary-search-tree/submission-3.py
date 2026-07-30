# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        if not root.left and not root.right:
            return True

        if root.left and root.right and root.val > root.left.val and root.val < root.right.val:
            self.isValidBST(root.left)
            self.isValidBST(root.right)
        else:
            return False
        return True
         
        

            