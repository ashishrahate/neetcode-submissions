# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # find the subroot in root . 
        # if not subRoot: return True
        # if not root: return False

        # queue = deque([root])
        # rootNode = TreeNode()
        # while queue:
        #     node = queue.popleft()
        #     if node and subRoot and node.val == subRoot.val:
        #         rootNode = node
        #         break
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return self.isTheSameTree(rootNode, subRoot)

        if not subRoot: return True  # An empty tree is always a subtree
        if not root: return False    # A non-empty subRoot cannot be a subtree of an empty root
        
        # If the trees are identical starting at the current node, return True
        if self.isTheSameTree(root, subRoot):
            return True
            
        # Otherwise, recursively check the left and right children of the root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # start comparing the tree from this root. 
    def isTheSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

        return self.isTheSameTree(p.left, q.left) and self.isTheSameTree(p.right, q.right)



        