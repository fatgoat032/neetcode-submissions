# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        dummy = ListNode()
        tail = dummy
        while current1 and current2:
            print(current1.val)
            if current1.val > current2.val:
                tail.next = current2
                current2 = current2.next
            else:
                tail.next = current1
                current1 = current1.next
            tail = tail.next
        tail.next = current1 or current2
        return dummy.next

        
        