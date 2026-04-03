# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            # Merge 2 lists and append to mergedlists array
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1,l2))
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        curr1 = list1
        curr2 = list2

        # Merge two lists
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
            # Move dummy pointer
            dummy = dummy.next
        # Append leftovers
        dummy.next = curr1 or curr2 

        # return sorted list
        return head.next

