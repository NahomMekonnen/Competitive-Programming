# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root) :
            if not root :
                return ""
            if not root.left and not root.right :
                return str(root.val)
            return str(dfs(root.left)) + "+" + str(dfs(root.right))
        return [i for i in dfs(root1).split("+") if i != ""] ==  [i for i in dfs(root2).split("+") if i != "" ]
