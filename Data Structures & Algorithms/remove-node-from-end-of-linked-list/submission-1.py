# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        x = 1
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        if n == 1:
            prev = prev.next
        else:
            node = prev
            while node:
                if x == n - 1:
                    node.next = node.next.next
                    break
                node = node.next
                x += 1
        curr = prev
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev