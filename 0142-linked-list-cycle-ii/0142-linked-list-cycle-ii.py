# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        
        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # no cycle
        
        # Step 2: Find entry point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

        