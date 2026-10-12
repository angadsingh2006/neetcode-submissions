# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        
        nodes.pop(len(nodes) - n)

        dummy = ListNode()
        tail = dummy

        for node in nodes:
            tail.next = ListNode(node)
            tail = tail.next
            
        return dummy.next