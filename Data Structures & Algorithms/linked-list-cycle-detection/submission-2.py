# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = second = head
        
        while second and second.next:
            second = second.next.next 
            first = first.next 

            if first == second:
                return True

        return False