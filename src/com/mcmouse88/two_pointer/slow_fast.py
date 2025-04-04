"""
    Slow and fast pointers are useful or detecting cycles, finding the middle
    of a structure or handling elements with different speeds. The most popular
    problems that can be solved using `Slow and fast` are detecting a cycle
    in linked list, find the middle of a linked list and other similar problems. 
"""

from typing import List, Optional
from ..structures.ListNode import ListNode

def find_duplicate(nums: List[int]) -> int:
    """
    ### Find the Duplicate Number

    Given an array of integers nums containing n + 1 integers where each integer
    is in the range [1, n] inclusive. There is only one repeated number in nums,
    return this repeated number. You must solve the problem without modifying
    the array nums and using only constant extra space.
 
    **Example 1:**
    > Input: nums = [1,3,4,2,2]
    Output: 2
    """
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    ### Linked List Cycle

    Given head, the head of a linked list, determine if the linked list has
    a cycle in it. There is a cycle in a linked list if there is some node
    in the list that can be reached again by continuously following the next
    pointer. Internally, pos is used to denote the index of the node that
    tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.

    **Example 1:**

    > Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects
    to the 1st node (0-indexed).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    ### Middle of the Linked List

    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.

    **Example 1:**

    > Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    ### Linked List Cycle II

    Given the head of a linked list, return the node where the cycle begins. If there is no cycle,
    return null.
    There is a cycle in a linked list if there is some node in the list that can be reached again 
    by continuously following the next pointer. Internally, pos is used to denote the index of the
    node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note
    that pos is not passed as a parameter.
    Do not modify the linked list.

    **Example 1:**

    > Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    """
    slow = fast = head
    while True:
        if fast is None or fast.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

l = ListNode(1)
print(has_cycle(l))