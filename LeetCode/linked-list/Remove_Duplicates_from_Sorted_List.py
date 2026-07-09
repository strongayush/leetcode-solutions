"""
Problem: Remove Duplicates from Sorted List
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=linked-list
Difficulty: Easy
Approach: use temp to traverse and don't move the temp if you found duplicate.
Time: |Space: 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        if head is None:
            return head
        elif head.next is None:
            return head
        else:
            temp = head
            while temp is not None and temp.next is not None:
                if temp.val == temp.next.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next 
            return head
        return head
