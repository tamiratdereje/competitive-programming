class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        
        group = defaultdict(set)
        queue = deque([(source, 0)])

        
        for ind, rout in enumerate(routes):
            
            for ro in rout:
                group[ro].add(ind)
                    
        
        visitedMember = set([source])
        visitedRoute = set()
        
        while queue:
            # bus, step
            cur, step = queue.popleft()
            
            if cur == target:
                return step
            
            for rou in group[cur]:
                if rou in visitedRoute:
                    continue
                for member in routes[rou]:
                    
                    if member not in visitedMember:
                        queue.append((member, step + 1))
                        visitedMember.add(member)
                        
                visitedRoute.add(rou)
                
        return -1
