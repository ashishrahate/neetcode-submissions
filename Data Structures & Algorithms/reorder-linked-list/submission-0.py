# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find the mid
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second  = slow.next
        prev = slow.next = None
        #reverse the second half of the list
        while second:    # because we know that the second list is going to be smaller in even and odd length case
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge the lists 
        first, second = head , prev # here prev is assigned because after the reversing the second will be pointing to the None
        
        while second:  # for the same reason as above
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        