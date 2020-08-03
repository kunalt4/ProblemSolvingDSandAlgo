class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [[] for _ in range(self.size) ]
        

    def add(self, key: int) -> None:
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)
        

    def remove(self, key: int) -> None:
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket, idx = self._index(key)
        return idx >= 0 
        
    def _index(self, key):
        hash = key % self.size
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#https://leetcode.com/problems/design-hashset/discuss/152654/Python-hash-set-with-trivial-hash-function
