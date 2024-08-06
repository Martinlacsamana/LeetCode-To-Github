class Solution:

    # Strat: Use Binary Search
    # Time Complexity: O(logn)
    # Space Complexity: O(1) -> Didn't allocate extra memory
    def search(self, nums: List[int], target: int) -> int:

        # Set our binary search boundaries
        left, right = 0, len(nums) - 1

        # Continue searching while the left pointer is less than or equal to the right pointer
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # If the target is not found, return -1
        return -1


        