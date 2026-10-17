# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        second = ""
        head = l1
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        while prev:
            first += str(prev.val)
            prev = prev.next
        head = l2
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        while prev:
            second += str(prev.val)
            prev = prev.next
        tot = int(first) + int(second)
        tot = str(tot)[::-1]
        nums = []
        dummy = ListNode()
        new = dummy
        for num in tot:
            nums.append(num)
        temp = new
        for num in nums:
            temp.next = ListNode(num)
            temp = temp.next
        return new.next
        
    
            
        
        