# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        maintain head pointers to the k lists [None, None, None]
        heap: [(1,0),(1,1),(3,2)] #(val_of_head, which_list)

        - pop (1, 0), update pointers [0+1,0,0], 
        get the next ListNode and heappush (2, 0)
        """
        
        ans = ListNode()
        ans_pointer = ans
        q = []
        k = len(lists)
        heads = [0] * k
        
        for i, node in enumerate(lists):
            if node:
                heads[i] = node
                heappush(q, (node.val, i))
        
        while q:
            val, list_idx = heappop(q)
            ans_pointer.next = ListNode(val)
            ans_pointer = ans_pointer.next

            node = heads[list_idx].next
            heads[list_idx] = node
            if node:
                heappush(q, (node.val, list_idx))

        return ans.next





        