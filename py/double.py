class LRUCache:

    class Node:
        def __init__(self,data = 0):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.head = self.Node()
        self.last = self.Node()
        self.dic = {}
        self.head.next = self.last
        self.last.prev = self.head
        self.size = capacity
        self.cur = 0

    def get(self, key: int) -> int:

        lruNode = self.head.next
        while lruNode != self.last and  lruNode.data != key:
            lruNode = lruNode.next
        if lruNode == self.last:
            return -1
        leftNode = lruNode.prev
        rightNode = lruNode.next
        leftNode.next = rightNode
        rightNode.prev = leftNode
        lastFirstNode = self.head.next
        self.head.next = lruNode
        lruNode.prev = self.head
        lruNode.next = lastFirstNode
        lastFirstNode.prev = lruNode
        return self.dic[key]


    def put(self, key: int, value: int) -> None:
        prev = self.head.next
        cur = self.Node(key)
        self.dic[key] = value
        self.head.next = cur
        cur.next = prev
        cur.prev = self.head
        prev.prev = cur
        self.cur += 1
        if self.cur > self.size:
            delete = self.last.prev
            newLast = delete.prev
            self.last.prev = newLast
            newLast.next = self.last
            self.cur = self.size


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)