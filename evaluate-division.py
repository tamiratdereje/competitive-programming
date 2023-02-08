class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        parent = {}
        size = {}
        graph = defaultdict(list)
        def find(child):
            if child == parent[child]:
                return child
            
            parent[child] = find(parent[child])
            
            return parent[child]
        
        
        def union(first, second):
            
            parent_first, parent_second = find(first), find(second)
            
            if parent_first != parent_second:
                
                if size[parent_first] < size[parent_second]:
                    parent_first, parent_second = parent_second, parent_first
                
                
                parent[parent_second] = parent_first
                size[parent_first] += size[parent_second]
        
        nodes = set()
        ans = []
        for ele in range(len(equations)):
            if equations[ele][0] not in size:
                size[equations[ele][0]] = 1
                parent[equations[ele][0]] = equations[ele][0]
            
            if equations[ele][1] not in size:
                size[equations[ele][1]] = 1
                parent[equations[ele][1]] = equations[ele][1]
                
            union(equations[ele][0], equations[ele][1])
            graph[equations[ele][0]].append((equations[ele][1], values[ele]))
            graph[equations[ele][1]].append((equations[ele][0], 1/values[ele]))
            
            nodes.add(equations[ele][0])
            nodes.add(equations[ele][1])
            
        def bfs(start, target):
            
            queue = deque([(start, 1)])
            visited = set([start])
            
            while queue:
                
                cur_node, cur_weight = queue.popleft()
                
                if cur_node == target:
                    return cur_weight
                
                for child, child_weight in graph[cur_node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append((child,cur_weight*child_weight))            
            return -1
                  
        for ele in range(len(queries)):
            
            if queries[ele][0] not in nodes or queries[ele][1] not in nodes:
                ans.append(float(-1))
                continue
            
            first = find(queries[ele][0])
            second = find(queries[ele][1])
            if first != second:
                ans.append(float(-1))
            else:
                ans.append(float(bfs(queries[ele][0],queries[ele][1])))
                
        return ans
