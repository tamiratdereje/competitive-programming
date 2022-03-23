# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        queue = collections.deque()
        self.layer = 1
        queue.append([root,1])
        avg = []
        currentMax = -math.inf
        avg.append(root.val)
        while queue:
            current, level = queue.popleft()
            if current.left != None:    
                queue.append([current.left, level+1])
            if current.right != None:
                queue.append([current.right, level+1])
            if level == self.layer:
                if current.left != None and current.left.val>currentMax:
                    currentMax = current.left.val
                if current.right != None and current.right.val>currentMax:    
                    currentMax = current.right.val
            if level > self.layer:  
                self.layer = level
                avg.append(currentMax)
                currentMax = -math.inf
                if current.left != None:
                    currentMax = current.left.val
                if current.right != None and current.right.val>currentMax: 
                    currentMax = current.right.val
        return avg
    
