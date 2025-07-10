# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = defaultdict(int)
        ptr = head
        while ptr :
            nums[ptr.val] += 1
            ptr = ptr.next
        valid = [i for i in nums if nums[i] == 1]
        valid.sort()
        ans = ListNode()
        prev = ans
