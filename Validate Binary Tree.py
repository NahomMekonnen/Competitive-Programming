# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inOrder(root, arr) :
            if not root :
                return
            inOrder(root.left, arr)
            arr.append(root.val)
            inOrder(root.right, arr)
        inOrder(root, arr)
        return sorted(arr) == arr and len(set(arr)) == len(arr)
