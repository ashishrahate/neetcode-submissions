# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        queue = deque([root])
        listToReturn = []

        while queue:
            currList = []
            for _ in range(len(queue)):
                node = queue.popleft()
                currList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            listToReturn.append(currList)

        return listToReturn
                








        # queueToReturn = deque([[root.val]])
        # while queue:
        #     item = queue.popleft()
        #     node = item[0]
        #     level = item[1]
        #     if node.left: 
        #         # queueToReturn.append([])
        #         if len(queueToReturn) == level:
        #             queueToReturn.append([node.left.val])
        #         else:
        #             queueToReturn[level].append(node.left.val)
        #         queue.append((node.left, level + 1))
        #     if node.right: 
        #         if len(queueToReturn) == level:
        #             queueToReturn.append([node.right.val])
        #         else:
        #             queueToReturn[level].append(node.right.val)
        #         queue.append((node.right, level +1))
        # return queueToReturn[0]






        