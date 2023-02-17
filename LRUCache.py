class LRUCache:
    def __init__(self, capacity: int):
        
        self.queue = deque([])
        self.dict_ = {}
        self.capacity = capacity
        self.size = 0
    
    def makeRecent(self, val):
        self.queue.remove(val)
        self.queue.append(val)
        
    def get(self, key: int) -> int:
        
        if key not in self.dict_:
            return -1
        else:
            self.makeRecent(key)
            return self.dict_[key]
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.dict_:
            self.makeRecent(key)
            self.dict_[key] = value
        
        else:
            
            if self.size < self.capacity:
                self.queue.append(key)
                self.size += 1
                self.dict_[key] = value
                
            else:
                if self.queue:
                    cur = self.queue[0]
                    self.queue.popleft()
                    del self.dict_[cur]
                    self.dict_[key] = value
                    self.queue.append(key)
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
