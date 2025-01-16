# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []

        def findHeight(root):

            if root is None:
                return 0

            leftHeight = 0
            rightHeight = 0

            leftHeight = findHeight(root.left)
            rightHeight = findHeight(root.right)

            return max(leftHeight,rightHeight)+1

        height = findHeight(root)

        def findlevels(root,level,node):
            if root is None:
                return node
            elif level == 1:
                node.append(root.val)
                return node
            else:
                node = findlevels(root.left,level-1,node)
                node = findlevels(root.right,level-1,node)

                return node


        for i in range(1,height+1):
            node = []
            node = findlevels(root,i,node)

            if i % 2 == 0:
                node.reverse()

            result.append(node)

        return result




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque
        if not root:
            return []
        queue = deque()

        queue.append(root)
        result = []
        count = 0

        while queue:
            levels = []
            count += 1

            for _ in range(len(queue)):

                node = queue.popleft()
                levels.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if count % 2 == 0:
                levels.reverse()

            result.append(levels)

        return result