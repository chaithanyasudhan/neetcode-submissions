# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter=max right nodes+left nodes
        s=0
        def dfs(root):
            nonlocal s#makes it global
            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            s=max(s,l+r)#stored max diameter
            return 1+max(l,r) #return height
        dfs(root)
        return s

        