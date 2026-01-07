# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        def tree_sum(node) :
            if not node :
                return 0
            return node.val + tree_sum(node.left) + tree_sum(node.right)
        total_sum = tree_sum(root)
        
        self.ans = 0
        def get_sum(node) :
            if not node :
                return 0
            subtree_sum = node.val + get_sum(node.left) + get_sum(node.right) 
            self.ans = max(self.ans,(total_sum - subtree_sum) * subtree_sum)
            return subtree_sum
        get_sum(root)
        return self.ans % MOD
