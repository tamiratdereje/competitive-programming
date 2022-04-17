

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if not head:
        return 0
    
    muke = head
    visited = set()
    lash =False
    while muke:
        if muke not in visited:
            visited.add(muke)
            muke = muke.next
        elif muke in visited:
            lash = True
            break
    if lash: return 1      
    return 0
    
    
    
