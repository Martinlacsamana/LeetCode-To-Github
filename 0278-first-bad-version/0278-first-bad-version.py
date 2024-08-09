# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution: 
    # Strat: Regular Binary Search
    # Time Complexity: O(LogN)
    # Space Complexity: O(N)
    def firstBadVersion(self, n: int) -> int:
        left , right = 1, n

        while left <= right:
            mid = (left + right) // 2

            # When we find the last bad one, the right pointer is what will be moved.
            # such that the left will then hold that value
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        # The min should be on the left variable
        return left
