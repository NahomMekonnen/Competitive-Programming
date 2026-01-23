# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp :
            size += 1
            temp = temp.next
        if size <= 1 and n >= 1 :
            return None
        temp = head
        if size == n :
            head = head.next
        while temp :
            if size == n + 1 :
                temp.next = temp.next.next
                break
            temp = temp.next
            size -= 1
        return head
