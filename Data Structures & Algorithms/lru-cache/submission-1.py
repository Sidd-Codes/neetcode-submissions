class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            temp = self.left.next.key
            self.remove(self.cache[temp])
            del self.cache[temp]
    
    def remove(self, node):
        temp = node.prev
        temp.next = node.next
        node.next.prev = temp
        
    def insert(self, node):
        next = self.right
        temp = self.right.prev
        temp.next = node
        node.prev = temp
        node.next = self.right
        self.right.prev = node