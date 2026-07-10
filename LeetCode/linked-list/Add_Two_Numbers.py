"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/description/?envType=problem-list-v2&envId=linked-list
Difficulty: Medium
Approach: Differnt From other questions we're using while l1 or l2 or carry and we are handaling everything from only one while loop
Time: | Space:
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10

            tail.next = ListNode(total % 10)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
