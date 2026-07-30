# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # find the subroot in root . 
        queue = deque([root])
        rootNode = TreeNode()
        while queue:
            node = queue.popleft()
            if node and subRoot and node.val == subRoot.val:
                rootNode = node
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return self.isTheSameTree(rootNode, subRoot)


    # start comparing the tree from this root. 
    def isTheSameTree(self, p: Optional[TreeNode], q: Optional[treeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

        return self.isTheSameTree(p.left, q.left) and self.isTheSameTree(p.right, q.right)



        