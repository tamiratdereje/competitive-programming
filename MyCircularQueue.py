class MyCircularQueue:

    def __init__(self, k: int):
        self.stack = []
        self.remove = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        
        if len(self.stack) + len(self.remove) == self.size:
            return False
        
        self.stack.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.remove and not self.stack:
            return False
        
        if self.remove:
            self.remove.pop()
            return True
            
        else:
            N = len(self.stack)
            
            for i in range(N-1,-1,-1):
                self.remove.append((self.stack.pop()))
            self.remove.pop()
            
            return True
        
    def Front(self) -> int:
        
        if self.stack and not self.remove:
            return self.stack[0]
        
        else:
            if self.remove:
                return self.remove[-1]
            else:
                return -1
            

    def Rear(self) -> int:
        
        if self.stack:
            return self.stack[-1]
        else:
            if self.remove:
                return self.remove[0]
            return -1

    def isEmpty(self) -> bool:
        return not self.remove and not self.stack

    def isFull(self) -> bool:
        return len(self.remove) + len(self.stack) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
