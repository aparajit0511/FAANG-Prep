# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiameter = 0
        Diameter = [0] # use this to update the variable inside recursion

        def findDiameter(root):
            nonlocal maxDiameter 

            if root is None:
                return 0

            leftHeight = 0
            rightHeight = 0

            leftHeight = findDiameter(root.left)
            rightHeight = findDiameter(root.right)

            maxDiameter = max(maxDiameter,(leftHeight+rightHeight))
            Diameter[0] = max(Diameter[0],(leftHeight+rightHeight))

            return 1 + max(leftHeight,rightHeight)

        findDiameter(root)

        return Diameter[0] 
        # return maxDiameter




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = []
        height = {}
        maxDiameter = 0

        stack.append((root,False))

        while stack:
            node , visited = stack.pop()

            if node:
                if visited:
                    
                    leftHeight = height.get(node.left,0)
                    rightHeight = height.get(node.right,0)

                    height[node] = max(leftHeight,rightHeight)+1
                    maxDiameter = max(maxDiameter,(leftHeight+rightHeight))

                else:
                    stack.append((node,True))
                    stack.append((node.right,False))
                    stack.append((node.left,False))

        return maxDiameter