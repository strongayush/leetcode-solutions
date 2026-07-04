"""
Problem: Reverse Integer
Link:https://leetcode.com/problems/reverse-integer/description/?envType=problem-list-v2&envId=math
Difficulty: Medium
Approach: Using '% 10' to split the digit from last and '// 10' to handle the 'while loop' which is the core.
Time: |Space: 
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev = sign * rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev 
