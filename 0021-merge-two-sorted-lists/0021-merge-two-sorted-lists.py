# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Time Complexity: O(n + m) - We iterate through all the nodes in both lists once.
    # Space Complexity: O(1) - We utilize the existing nodes without allocating additional space for new nodes.

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize a dummy node to serve as the head of the merged list
        head = ListNode(0)
        ans = head
        
        # Iterate through both lists until one of them is exhausted
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        # Attach the remaining nodes from the non-exhausted list
        head.next = list1 or list2

        # Return the merged list, which starts from the next of dummy node
        return ans.next
