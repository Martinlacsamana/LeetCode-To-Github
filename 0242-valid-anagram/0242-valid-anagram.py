class Solution:
    # Strat: Use a counter map to increment/decrement
    
    # Time Complexity: O(n) - We iterate throgh the nodes once.
    # Space Complexity: O(n) - We open up n frames for the recursion.

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        # store letters of s into a HashMap
        ctr = defaultdict(int)
        for letter in s:
            ctr[letter] += 1
        
        for letter in t:
            ctr[letter] -=1
        
        # all val should be 0
        for val in ctr.values():
            if val != 0: return False
        return True


        