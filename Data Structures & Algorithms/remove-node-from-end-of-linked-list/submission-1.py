# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        second = result
        first = head

        # Give first pointer head start
        for i in range(n):
            first = first.next
        
        # Move 2 pointers until the faster one reaches null
        while first != None:
            first = first.next
            second = second.next

        # Remove node
        second.next = second.next.next
        return result.next
                