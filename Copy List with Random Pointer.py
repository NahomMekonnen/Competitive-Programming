"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newList = Node(0)
        t1, t2 = head, newList
        nodes = {}
        while t1 :
            t2.next = Node(t1.val)
            t2 = t2.next
            nodes[t1] = t2
            t1 = t1.next
        newList = newList.next
        t1, t2 = head, newList
        while t1 :
            if t1.random :
                t2.random = nodes[t1.random]
            t1 = t1.next
            t2 = t2.next

        return newList
        
