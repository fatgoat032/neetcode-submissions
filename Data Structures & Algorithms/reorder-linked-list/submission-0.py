# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        front = head
        while front and front.next:
            rest = front.next
            front.next = None
            prev = None
            curr = rest
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            front.next = prev
            front = front.next

            
       