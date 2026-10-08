# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #use bottom up approach using postorder traversal
        f=1
        def balance(root):
            nonlocal f
            if not root:
                return 0# when reachin none height=0
            l=balance(root.left)

            r=balance(root.right)
            if abs(l-r)>1:
                f=0
            return 1+max(l,r)
        a=balance(root)
        if f==0:
            return False
        elif f==1:
            return True

            
        