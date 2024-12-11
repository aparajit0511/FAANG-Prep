# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def findHeight(root):
            if root is None:
                return 0
            else:
                left_height = 0
                right_height = 0

                left_height = findHeight(root.left)
                right_height = findHeight(root.right)

                if left_height >= right_height:
                    return left_height + 1
                else:
                    return right_height + 1

        
        return findHeight(root)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if root is None:
            return 0

        queue = deque()
        queue.append((root,0))
        maxDepth = 0

        while queue:

            item , depth = queue.popleft()
            maxDepth = max(maxDepth,depth)

            if item.left:
                queue.append((item.left,depth+1))

            if item.right:
                queue.append((item.right,depth+1))

        return maxDepth+1

