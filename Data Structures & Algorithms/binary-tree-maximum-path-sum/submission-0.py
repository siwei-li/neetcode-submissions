# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = [root.val]
        
        @functools.cache
        def maxSum(node, root_in_upstream):
            if not node:
                return 0
            global_max[0] = max(global_max[0], node.val)
            
            ans = 0
            l_oneside, r_oneside = maxSum(node.left, True), maxSum(node.right, True)
            ans = max(0, node.val, node.val + l_oneside, node.val + r_oneside)
            # print('one_side', ans)
            
            if not root_in_upstream:
                l_twosides, r_twosides = maxSum(node.left, False), maxSum(node.right, False)
                ans = max((ans, node.val + l_oneside + r_oneside, l_twosides, r_twosides))
                # print('two_sides', ans)
            # print(node.val, root_in_upstream, ans)
            return ans
        
        ans = maxSum(root, False)
        if ans == 0 and global_max[0] < 0:
            return global_max[0]
        return ans
        