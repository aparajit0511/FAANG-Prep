# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None  

        root.left , root.right = root.right , root.left

        self.invertTree(root.left)
        self.invertTree(root.right)          

        return root



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        from collections import deque
        queue = deque()

        queue.append(root)

        while queue:
            item = queue.popleft()

            item.left , item.right = item.right , item.left

            if item.left:
                queue.append(item.left)

            if item.right:
                queue.append(item.right)

        return root