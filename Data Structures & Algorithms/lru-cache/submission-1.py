class Node:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next, self.prev = None, None

class LRUCache:
    """
    map = {key: node(key, val)}
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dl = Node()
        
        self.size = 0
        self.map = {}
        # Sentinel Nodes
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        
    def add_node_to_end(self, node):
        A = self.right.prev
        A.next = node
        node.prev = A
        node.next = self.right
        self.right.prev = node
    
    def del_node_from_start(self):
        new_head = self.left.next.next
        self.left.next = new_head
        new_head.prev = self.left

    def move_node_to_end(self, node):
        A, B = node.prev, node.next
        A.next = B
        B.prev = A

        self.add_node_to_end(node)


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.move_node_to_end(self.map[key])

        # print(self.left.next.key, self.right.prev.key)
        return self.map[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # 1. update the node val; 2. move the node to the end
            node = self.map[key]
            node.val = value
            self.move_node_to_end(node)
        else:
            node = Node(key = key, val = value)
            self.size += 1
            self.map[key] = node
            self.add_node_to_end(node)
            # print(self.map, self.size, self.left.next.key, self.right.prev.key)

            if self.size > self.capacity:
                # DONE remove the oldest node; get its key
                d_key = self.left.next.key
                del self.map[d_key]
                self.del_node_from_start()
                self.size -= 1

        # print(self.left.next.key, self.right.prev.key)



        
