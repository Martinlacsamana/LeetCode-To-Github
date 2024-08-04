class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the numbers we have seen and their indices
        seen = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # Check if the difference is already in the dictionary
            if diff in seen:
                # If found, return the current index and the index of the difference
                return [index, seen.get(diff)]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = index

        # Time Complexity: O(n), as we traverse the list once
        # Space Complexity: O(n), as we store each number in the dictionary

        