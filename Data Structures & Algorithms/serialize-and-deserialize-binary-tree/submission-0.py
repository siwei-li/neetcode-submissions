# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "" 
        
        node_q = [root]
        ans = [str(root.val)]
        new_node_q = []
        while node_q:
            for n in node_q:
                if n.left:
                    new_node_q.append(n.left)
                    ans.append(str(n.left.val))
                else:
                    ans.append("")

                if n.right:
                    new_node_q.append(n.right)
                    ans.append(str(n.right.val))
                else:
                    ans.append("")
            
            node_q = new_node_q
            new_node_q = []
            # print(node_q)
        
        # print(ans)
        return ",".join(ans)

      
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # maintain two levels of leaf nodes

        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        
        node_level = [root]
        new_node_level = []
        i = 0
        while node_level:
            for n in node_level:
                i += 1
                # print(i, vals[i])
                if vals[i]:
                    l = TreeNode(int(vals[i]))
                    n.left = l
                    new_node_level.append(l)
                i += 1
                # print(i, vals[i])
                if vals[i]:
                    r = TreeNode(int(vals[i]))
                    n.right = r
                    new_node_level.append(r)
            node_level = new_node_level
            new_node_level = []
        
        return root
