# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        n = set(nums)
        newHead = ListNode(0)
        curr = newHead
        temp = head
        while temp :
            if temp.val not in n :
                curr.next = ListNode(temp.val)
                curr = curr.next
            temp = temp.next
        return newHead.next

        
