# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return head
        curr = head
        dq = deque()
        s = 0
        while curr :
            dq.append(curr.val)
            s += 1
            curr = curr.next
        for i in range(k%s) :
            dq.appendleft(dq.pop())
        newHead = ListNode(0)
        temp = newHead
        while dq :
            temp.next = ListNode(dq.popleft())
            temp = temp.next
        return newHead.next
