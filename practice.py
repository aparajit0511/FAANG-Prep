# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        from collections import deque
        queue = deque()
        queue.append(root)
        
        parent = {root.val:None}

        while p not in parent or q not in parent:

            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parent[node.left.val] = node.val

            if node.right:
                queue.append(node.right)
                parent[node.right.val] = node.val


        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q

