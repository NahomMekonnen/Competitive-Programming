# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        t = head
        while t : 
            arr.append(t.val)
            t = t.next
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        t, i = head, 0
        while t :
            if t.val != arr[i] :
                t.val = arr[i]
            i += 1
            t = t.next
        return head 