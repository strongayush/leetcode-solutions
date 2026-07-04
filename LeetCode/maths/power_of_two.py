"""
Problem: Power Of Two
Link: https://leetcode.com/problems/power-of-two/description/?envType=problem-list-v2&envId=math
Difficulty: Easy
Approach: let n = 2^x then bitwise operation of 'n & n-1' will always give 0. & -> bitwise 'and' operator
Time: |Space: 
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.n = n
        if self.n > 0 and (self.n & self.n-1 == 0):
            return True
        else:
            return False
