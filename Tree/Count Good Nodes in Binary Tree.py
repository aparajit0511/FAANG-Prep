# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        def countNodes(root,count,max_val):
            if root is None:
                return count

            if root.val >= max_val:
                max_val = root.val
                count += 1

            count = countNodes(root.left,count,max_val)
            count = countNodes(root.right,count,max_val)
            max_val = root.val

            return count

        return countNodes(root,0,root.val)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        from collections import deque
        queue = deque()

        queue.append((root,root.val))
        count = 0

        while queue:

            item,max_val = queue.popleft()
            if item:
                if item.val >= max_val:
                    count += 1
                new_max_val = max(max_val,item.val)

                if item.left:
                    queue.append((item.left,new_max_val))
         

                if item.right:
                    queue.append((item.right,new_max_val))


        return count