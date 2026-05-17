# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # p = head
        # while p.next:
        #     p = p.next
        # p.next = ListNode()

        if not head:
            return head
        
        d = ListNode()
        d.next = head

        A = head
        B = head
        C = B.next
        
        while C:
            D = C.next
            d.next = C
            C.next = A
            B.next = D
            A = C
            C = D
        
        return d.next


            

        