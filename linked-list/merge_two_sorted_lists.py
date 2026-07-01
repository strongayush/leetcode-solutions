"""
Problem: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=linked-list
Difficulty: Easy
Approach: Use a dummy node and two pointers to merge nodes in sorted order, then attach whichever list remains
Time: | Space:
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = list1
        temp2 = list2
        dummy = ListNode(-1)
        tail = dummy

        while temp1 and temp2:
            if temp1.val < temp2.val:
                tail.next = temp1
                temp1 = temp1.next
            else:
                tail.next = temp2
                temp2 = temp2.next
            tail = tail.next  

        tail.next = temp1 if temp1 else temp2
        return dummy.next
