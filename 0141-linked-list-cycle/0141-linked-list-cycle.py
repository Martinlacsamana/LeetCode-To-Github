# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Strat: Use fast and slow pointers to determine if a cycle
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None
        while fast and fast.next:
            if fast == slow:    # means found a cycle
                return True
            slow = slow.next
            fast = fast.next.next

        return False # if we get here then no cycle
