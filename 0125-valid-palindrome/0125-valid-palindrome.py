# STRAT -> two pointers and check if they're the same, return false if not
# Time Complexity -> O(n)
# Space Complexity -> O(1) -> didn't use shit for these two pointers

# Optimized solution, create a new string and make sure c.isalnum AND return True if string == string[::-1] else False -> just saying if front is equal to opposite

class Solution:
    # Time Complexity: O(n) - We iterate through the string a constant number of times.
    # Space Complexity: O(1) 

    def isPalindrome(self, s: str) -> bool:
       
         # Filter out non-alphanumeric characters and convert to lowercase
        s = [letter.lower() for letter in s if letter.isalnum()]

        # Check if the string is equal to its reverse using a generator expression
        return all(s[i] == s[~i] for i in range(len(s) // 2))
    

