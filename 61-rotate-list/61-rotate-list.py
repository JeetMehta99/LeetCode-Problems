# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        length = 1
        tail = head
        # print(tail)
        
        while tail.next:
            tail = tail.next
            # print(tail)
            length += 1
        
        k %= length
        # print(k)
        
        if k == 0:
            return head

        # new head will always start from length - k
        # attach tail->next to head and find new head now relative to tail position 
        steps_to_new_head = length - k
        tail.next = head
        # print(tail)
        
        while steps_to_new_head > 0:
            tail = tail.next
            steps_to_new_head -= 1
        
        # make new_head point to tail.next
        # and point tail->next to NULL
        new_head = tail.next
        tail.next = None
        
        return new_head