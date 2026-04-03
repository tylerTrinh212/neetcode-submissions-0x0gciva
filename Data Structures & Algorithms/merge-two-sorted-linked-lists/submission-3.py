# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        curr1 = list1
        curr2 = list2

        newList = ListNode()
        dummy = newList
        while curr1 and curr2:
            if curr1.val < curr2.val:
                newList.next = curr1
                curr1 = curr1.next
                newList = newList.next
            else:
                newList.next = curr2
                curr2 = curr2.next
                newList = newList.next


        #If one list still has entries append to list
        if curr1:
            newList.next = curr1
        elif curr2:
            newList.next = curr2
        return dummy.next