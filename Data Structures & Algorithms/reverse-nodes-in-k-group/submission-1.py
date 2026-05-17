# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        from dummy (A):
        1 step: C
        k steps: B (must not be None)
        k+1 steps: D (could be None)

        then C becomes the new A
        """

        d = ListNode()
        d.next = head
        A = d
        
        while A:
            pointer = A
            for i in range(k):
                pointer = pointer.next
                if not pointer:
                    return d.next
            
            B = A.next
            C = B
            D = C.next
            if D:
                E = D.next
            # print(A.val, B.val, C.val, D.val, E.val if E else None)
            for i in range(k-1):
                A.next = D
                D.next = B
                C.next = E
                B = D
                D = E
                if D:
                    E = D.next
                # print(i, A.val, B.val, C.val, D.val, E.val if E else None)
            
            A = C
            
        return d.next
            
            