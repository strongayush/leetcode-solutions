"""
Problem: Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/description/?envType=problem-list-v2&envId=math
Difficulty: Easy
Approach: Convert the int into str and then used the slice notation to check if it's Panlindrome
Time: |Space: 
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = str(x)
        if self.x[::1] == self.x[::-1]:
            return True
        else:
            return False
