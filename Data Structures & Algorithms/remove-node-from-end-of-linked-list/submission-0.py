# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head
        length = 1
        while first : 
            first = first.next 
            length += 1
        i = 1
        prev , second = None, head
        while i < (length - n):
            prev = second
            second = second.next
            i+= 1
        if prev : 
            prev.next = second.next
        else:  
            head = head.next
            
        second.next = None

        return head
        

        


        