# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        n1, n2 = "", ""
        t1, t2 = l1, l2 

        while t1 :
            n1 += str(t1.val)
            t1 = t1.next
        while t2 :
            n2 += str(t2.val)
            t2 = t2.next
        
        n3 = str(int(n1) + int(n2)) 

        l3 = ListNode(0)
        t3 = l3
        for i in n3 :
            t3.next = ListNode(int(i))
            t3 = t3.next
        l3 = l3.next
        return l3