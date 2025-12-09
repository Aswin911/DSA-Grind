# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        itr = head
        N = 0

        while itr:
            N += 1 
            itr = itr.next
        
        index = N-n

        prev = dummy
        cur = head
        count = 0
        while cur:
            if count == index:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
            count += 1

        return dummy.next