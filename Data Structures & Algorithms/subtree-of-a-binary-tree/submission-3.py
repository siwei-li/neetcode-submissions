# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools

class Solution: 
    @functools.cache  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(node, subnode):
        
            if not node or not subnode: 
                return node == subnode
            if node.val != subnode.val:
                return False
            return is_same_tree(node.left, subnode.left) and is_same_tree(node.right, subnode.right)

        def helper(node, subnode):
            if not node: return False
            if is_same_tree(node, subnode):
                return True
            return helper(node.left, subnode) or helper(node.right, subnode)
        
        return helper(root, subRoot)
        
        


