# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p.val == q.val and root.val == q.val:
        #     return root
        
        # if not root: return root
        
        # if root:
        #     if (root.val == p.val or root.val == q.val):
        #         if root.left.val == p.val or root.left.val == q.val or root.right.val == p.val or root.right.val == q.val:
        #             return root
        #     else:
        #         if (root.left.val == p.val and root.right.val == q.val) or (root.right.val == p.val and root.left.val == q.val):
        #             return root
        #     self.lowestCommonAncestor(root.left, p, q)
        #     self.lowestCommonAncestor(root.right, p, q)

        if not root: return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root



        