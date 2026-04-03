# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        # New linked list
        result = ListNode(0)
        head = result

        while curr1 != None and curr2 != None:
            
            if curr1.val <= curr2.val:
                result.next = curr1
                curr1 = curr1.next
                
            else:
                result.next = curr2
                curr2 = curr2.next
            # Move result pointer
            result = result.next

        # Append leftover nodes
        result.next = curr1 or curr2

        return head.next
