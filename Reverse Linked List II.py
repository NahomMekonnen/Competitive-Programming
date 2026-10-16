# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right :
            return head 
        arr = []
        p = head
        while p :
            arr.append(p.val)
            p = p.next  
        left -= 1
        right -= 1
        
        arr = arr[:left] + arr[left: right + 1][::-1] + arr[right + 1:]
        
        head = ListNode(0)
        p = head
        for i in arr :
            p.next = ListNode(i)
            p = p.next
        head = head.next
        return head