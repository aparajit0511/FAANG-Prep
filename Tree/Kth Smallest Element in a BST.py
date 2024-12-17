# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []
        count = 0
        
        while True:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1
            if count == k:
                break

            current = current.right

        return current.val



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        def findInorder(root,inorder,k):
            if root is None:
                return inorder
            else:
                inorder = findInorder(root.left,inorder,k)
                inorder.append(root.val)

                inorder = findInorder(root.right,inorder,k)

                return inorder

        inorder = findInorder(root,[],k)

        return inorder[k-1]
