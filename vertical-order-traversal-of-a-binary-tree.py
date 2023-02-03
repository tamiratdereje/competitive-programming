# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        queue = deque([(root, 0, 0)])
        level = 0
        while queue:
            cur_node, depth, col = queue.popleft()

            if not cur_node: continue
                           
            result.append((col,depth, cur_node.val))
            
            queue.append((cur_node.left, depth + 1, col - 1 ))
            queue.append((cur_node.right, depth + 1, col + 1))
      
        result.sort()
        ans = []
        first = result[0][0]
        temp = []
        for ele in result:
            
            if first == ele[0]:
                temp.append(ele[2])
            else:
                ans.append(temp)
                first = ele[0]
                temp = [ele[2]]
                
        ans.append(temp)  
        return ans  
        
        
