class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = defaultdict(int)
        
        for first, second in edges:
            indegree[second] += 1
        ans = []
        for ele in range(n):
            if not indegree[ele]:
                ans.append(ele)
        
        return ans
