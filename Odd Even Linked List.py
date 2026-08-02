# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        odds, evens = ListNode(0), ListNode(0)
        t1, t2, = odds, evens
        turn = 1 
        while temp :
            if turn % 2 == 0 :
                t2.next = ListNode(temp.val)
                t2 = t2.next
            else :
                t1.next = ListNode(temp.val)   
                t1 = t1.next
            turn += 1
            temp = temp.next
        odds = odds.next
        evens = evens.next
        t1.next = evens
        return odds
