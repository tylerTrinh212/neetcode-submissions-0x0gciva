# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        newSet = set()

        # Iterate through list, if the next pointer points to prev node, return its index
        while head:
            if head not in newSet:
                newSet.add(head)
                head = head.next
            else:
                return True
        return False
