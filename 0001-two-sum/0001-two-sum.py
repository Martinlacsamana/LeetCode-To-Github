class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Just to see what happens here 
        seen = {}
        # add the difference (key) and index of the number
        for index, num in enumerate(nums):
            # check if target - num is in hashmap
            diff = target - num
            if diff in seen:
                return [index, seen.get(diff)]
            
            # else, just add to hashmap
            seen[num] = index
        
        # NOTES
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Check to see if the complement -> target - num is in the hashmap
        # If not, just add the number to this dictionary