# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []

        curr = head

        while curr:
            nodes.append(curr.val)
            curr = curr.next
        
        nodes.pop(len(nodes) - n)
        
        dummy = ListNode()
        cur = dummy

        for num in nodes:
            cur.next = ListNode(num)
            cur = cur.next
        
            
        return dummy.next
