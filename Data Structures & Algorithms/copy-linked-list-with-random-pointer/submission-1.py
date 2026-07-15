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
        if not head:
            return None

        # Pass 1: Create copy nodes
        curr = head
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        # Pass 2: Copy random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Pass 3: Separate the two lists
        curr = head
        newHead = head.next
        newcurr = newHead

        while curr:
            curr.next = newcurr.next
            curr = curr.next

            if curr:
                newcurr.next = curr.next
                newcurr = newcurr.next

        return newHead