#leetcode 8

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0  # Return 0 for empty string
        
        i = 0
        ans = 0
        negative = 1
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Skip leading whitespaces
        while i < len(s) and s[i] == " ":
            i += 1
        
        # Check for sign
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            negative = -1 if s[i] == "-" else 1
            i += 1
        
        # Process numeric characters
        while i < len(s) and s[i].isdigit():
            if ans > (INT_MAX - int(s[i])) # Check for overflow
                return INT_MAX if negative == 1 else INT_MIN
            ans = ans * 10 + int(s[i])
            i += 1
        
        return ans * negative
