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
        old_to_new = {None: None}
        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            cp = old_to_new[node]
            cp.next = old_to_new[node.next]
            cp.random = old_to_new[node.random]
            node = node.next
        return old_to_new[head]
        
    
        