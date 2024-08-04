class Solution(object):
    # STRATEGY -> Iterate through symbols checking for closing symbols and only adding opening symbols to the stack.
    # Using a HashMap to hold symbol pairings for clarity, but hardcoding is also an option.
    
    # Time Complexity: O(n) - We iterate through the string once.
    # Space Complexity: O(n) - In the worst case, the stack could contain all opening symbols.

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Define the pairings
        matches = {')': '(', '}': '{', ']': '['}
        stack = []
        

        for symbol in s:
            # If the symbol is a closing bracket
            if symbol in matches:
                # If stack is empty or the top of the stack is not the matching opening bracket, return False
                if not stack or stack.pop() != matches[symbol]:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(symbol)

        # If the stack is empty, all the brackets were matched correctly
        return not stack