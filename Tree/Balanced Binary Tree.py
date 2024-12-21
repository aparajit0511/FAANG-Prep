# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def findHeight(root,left_height,right_height):

            if root is None:
                return True
            else:

                print(root.val,left_height,right_height)

                bool = findHeight(root.left,left_height+1,right_height)
                bool = findHeight(root.right,left_height,right_height+1)

                if left_height > right_height+1 or right_height > left_height+1 or left_height == right_height:
                    return False

                return True

        return findHeight(root.left,0,0) and findHeight(root.right,0,0)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        if root is None:
            return True

        if not root.left and not root.right:
            return True

        queueL = deque()
        queueR = deque()

        depthL , depthR = 0 , 0

        if root.left:
            queueL.append((root.left,0))
            depthL = self.findHeight(queueL,0) + 1

        if root.right:
            queueR.append((root.right,0))
            depthR = self.findHeight(queueR,0) + 1
     
        print(depthL,depthR)

        if depthL > depthR+1 or depthR > depthL+1 or depthL == depthR:
            return False

        return True

    def findHeight(self,queue,depth):
        # print("hi")

        while queue:
            item , depth = queue.popleft()

            if item.left:
                queue.append((item.left,depth+1))

            if item.right:
                queue.append((item.right,depth+1))

        # print(depth)

        return depth


