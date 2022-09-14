# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head
        
        curr = head.next
        
        temp = ListNode(-1, head)
        
        while curr:
            j_prev, j, cur_next = temp, temp.next, curr.next
            
            if curr.val > prev.val:
                prev = curr
                
            else:
                while j.val < curr.val:
                    j_prev, j = j, j.next
                    
                curr.next = j
                j_prev.next = curr
                
                prev.next = cur_next
                
            curr = cur_next
            
        return temp.next
