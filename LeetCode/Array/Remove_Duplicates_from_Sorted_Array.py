"""
Problem: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=array
Difficulty: Medium
Approach: just declear a variable i = 0 and use the condidition while i < len(_name of you array_) - 1
Time: |Space:
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)
