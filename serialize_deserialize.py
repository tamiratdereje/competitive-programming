# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        # iterate in preorder traversal
        
        """Encodes a tree to a single string.
        """
        
        def dfs(node):
            if not node:
                return ['*']
            
            return [str(node.val)] + dfs(node.left) + dfs(node.right)
        
        ans = dfs(root)
        # print(",".join(ans))
        return ",".join(ans)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        """Decodes your encoded data to tree.
        """
        data = data.split(',')
        def dfs(ind = 0):
            
            # print(ind)
            if data[ind] == '*':
                return None, ind+1
            
            cur_node = TreeNode()
            cur_node.val = data[ind]
            
            left_node, left_ind = dfs(ind+1)
            right_node, right_ind = dfs(left_ind)
            
            cur_node.left = left_node
            cur_node.right = right_node
            
            
            return cur_node, right_ind
        
        ans = dfs()
        # print(ans)
        return ans[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
