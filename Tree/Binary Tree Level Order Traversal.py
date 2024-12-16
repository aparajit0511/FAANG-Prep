# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        from collections import deque

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            level = []
            
            for _ in range(len(queue)):
                item = queue.popleft()
                level.append(item.val)

                if item.left:
                    queue.append(item.left)                   

                if item.right:
                    queue.append(item.right)

            result.append(level)

        return result




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
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

                return right_height + 1

        height = findHeight(root)
        result = []

        def findLevelOrder(root,level,nodes):
            if root is None:
                return nodes
            if level == 1:
                nodes.append(root.val)
            elif level > 1:
                nodes = findLevelOrder(root.left,level-1,nodes)
                nodes = findLevelOrder(root.right,level-1,nodes)
            return nodes

        for i in range(1,height+1):
            nodes = []
            nodes = findLevelOrder(root,i,nodes)
            result.append(nodes)

        return result