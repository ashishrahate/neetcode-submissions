# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxdep, currdep = 1, 1
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left or node.right:
                currdep += 1
                maxdep = max(maxdep, currdep)
                print(currdep, maxdep)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return maxdep
        