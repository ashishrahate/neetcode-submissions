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
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left or node.right:
                currdep += 1
                maxdep = max(maxdep, currdep)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return maxdep
        