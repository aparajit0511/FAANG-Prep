# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def checkSameTree(root1,root2):

            if root1 is not None and root2 is None:
                return False

            if root1 is None and root2 is not None:
                return False

            if root1 is None and root2 is None:
                return True

            if root1 and root2:
                return checkSameTree(root1.left,root2.left) and checkSameTree(root1.right,root2.right) and root1.val == root2.val
            else:
                return False
            
            return True

            

        return checkSameTree(p,q)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkInorder(root,inorder):

            if root is None:
                return inorder
            else:
                inorder = checkInorder(root.left,inorder)
                inorder.append(root.val)
                inorder = checkInorder(root.right,inorder)

                return inorder

            inorder1 = []
            inorder2 = []
            inorder1 = checkInorder(p,inorder1)
            inorder2 = checkInorder(q,inorder2)

            if len(inorder1) != len(inorder2):
                return False

            for i in range(len(inorder1)):
                if inorder1[i] != inorder2[i]:
                    return False

            return True