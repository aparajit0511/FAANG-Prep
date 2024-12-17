# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        
        inorder = []

        def findInorder(root,inorder):

            if root is None:
                return inorder
            else:

                inorder = findInorder(root.left,inorder)
                inorder.append(root.val)
                inorder = findInorder(root.right,inorder)

                return inorder

        inorder = findInorder(root,inorder)  

        for i in range(len(inorder)-1):

            if inorder[i] >= inorder[i+1]:
                return False

        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        current = root
        stack = []
        inorder = []

        while True:

            if current is None and not stack:
                break

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            inorder.append(current.val)

            current = current.right

        for i in range(len(inorder)-1):

            if inorder[i] >= inorder[i+1]:
                return False

        return True
