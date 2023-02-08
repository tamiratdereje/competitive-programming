class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(set)
        inDegree = defaultdict(int)
        
        for first, second in adjacentPairs:
            
            graph[first].add(second)
            graph[second].add(first)
            inDegree[first] += 1
            inDegree[second] += 1
        
        first = 0
        last = 0
        getIt = False
        
        for ele in inDegree:
            if not getIt and inDegree[ele] == 1:
                first = ele
                getIt = True
            
            if getIt and inDegree[ele] == 1:
                last = ele
        
        queue = deque([first])
        ans = []
        
        while queue:
            cur = queue.popleft()
            
            ans.append(cur)
            
            for ele in graph[cur]:
                
                inDegree[ele] -= 1
                graph[ele].remove(cur)
                
                if inDegree[ele] == 1:
                    queue.append(ele)
        
        ans.append(last)
        
        return ans              
