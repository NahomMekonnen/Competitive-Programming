# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        t = head
        nodes = []
        while t :
            nodes.append(t.val)
            t = t.next
        n = len(nodes)
        ans = [0] * n
        stack = deque([])
        for i in range(n - 1, -1, -1) :
            while len(stack) > 0 and stack[-1] <= nodes[i] :
                stack.pop()
            if len(stack) > 0 :
                ans[i] = stack[-1]
            stack.append(nodes[i])
            
        return ans

      