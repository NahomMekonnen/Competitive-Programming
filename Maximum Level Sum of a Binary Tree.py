# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        ans = float('-inf')
        q.append(root) 
        levels = []
        while q :
            qLen = len(q)
            total = 0
            level = []
            for _ in range(qLen) :
                node = q.popleft()
                if node :
                    total += node.val
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level == [] :
                break
            level.append(total)
            levels.append(level)
            ans = max(ans, total)
        for i in range(len(levels)) :
            if levels[i][-1] == ans :
                return i + 1
        return 0
