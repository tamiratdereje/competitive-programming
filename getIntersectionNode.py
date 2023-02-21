# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def move(node, diff):
            
            while diff > 0:
                
                diff -= 1
                node = node.next
            
            return node
        
            
        a_len = 0
        b_len = 0
        first = headA
        second = headB
        
        while first:
            first = first.next
            a_len += 1
        while second:
            second = second.next
            b_len += 1
        
        diff = abs(a_len - b_len)
        first = move(headA, a_len - b_len )
        second = move(headB, b_len - a_len )
        while first and second:
            
            if first == second:
                return first
            first = first.next
            second = second.next
        
        return None
        
        
