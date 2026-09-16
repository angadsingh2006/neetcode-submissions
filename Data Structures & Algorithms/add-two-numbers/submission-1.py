# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        first, second = l1, l2
        carry = 0

        dummy = ListNode()
        curr = dummy

        while first or second or carry:
            val1 = first.val if first else 0
            val2 = second.val if second else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if first:
                first = first.next
            if second:
                second = second.next
        
        return dummy.next
