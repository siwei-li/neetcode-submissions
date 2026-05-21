# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def iterate(node):
            nonlocal cnt
            
            # if not node:
            #     return -1
            if node.left:
                r = iterate(node.left)
                if r != -1:
                    return r
            cnt += 1
            # print(cnt, node.val)
            if cnt == k:
                # print("k")
                return node.val
            if node.right:
                r = iterate(node.right)
                if r != -1:
                    return r
            return -1
        return iterate(root)
        