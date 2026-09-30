class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2


"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


"""
# Dry run for list1 = [1,2,4], list2 = [1,3,4]

mergeTwoLists(1→2→4, 1→3→4)
├─ list1.val (1) < list2.val (1)? → NO
├─ list2.next = mergeTwoLists(1→2→4, 3→4)
│  ├─ list1.val (1) < list2.val (3)? → YES
│  ├─ list1.next = mergeTwoLists(2→4, 3→4)
│  │  ├─ list1.val (2) < list2.val (3)? → YES
│  │  ├─ list1.next = mergeTwoLists(4, 3→4)
│  │  │  ├─ list1.val (4) < list2.val (3)? → NO
│  │  │  ├─ list2.next = mergeTwoLists(4, 4)
│  │  │  │  ├─ list1.val (4) < list2.val (4)? → NO
│  │  │  │  ├─ list2.next = mergeTwoLists(4, None)
│  │  │  │  │  ├─ list2 is None → return list1 (4)
│  │  │  │  │  ← returns 4
│  │  │  │  └─ list2.next = 4, return list2 (4→4)
│  │  │  └─ list2.next = 4→4, return list2 (3→4→4)
│  │  └─ list1.next = 3→4→4, return list1 (2→3→4→4)
│  └─ list1.next = 2→3→4→4, return list1 (1→2→3→4→4)
└─ list2.next = 1→2→3→4→4, return list2 (1→1→2→3→4→4)

Output: [1,1,2,3,4,4] ✓

"""
