# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_range(node):
            if not node:
                return (None, None, True)
            
            r = [node.val, node.val, True]
            left_min, left_max, res_l = get_range(node.left)
            if not res_l or (left_max and left_max >= node.val):
                return (None, None, False)
            if left_min:
                r[0] = left_min
            
            right_min, right_max, res_r = get_range(node.right)
            if not res_r or (right_min and right_min <= node.val):
                return (None, None, False)
            if right_max:
                r[1] = right_max
            
            # print(node.val, r)
            return r
        
        return get_range(root)[-1]

        