class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0, 1, 0))
        while q:
            pos, speed, n = q.popleft()
            if pos == target:
                return n
            q.append((pos+speed, speed*2, n+1))
            if speed > 0:
                if pos + speed > target:
                    q.append((pos, -1, n+1))
            else:
                if pos + speed < target:
                    q.append((pos, 1, n + 1))
        
