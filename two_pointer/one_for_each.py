from typing import List

"""
    One for each is useful when given two or more arrays and you need to check or take one element from each 
    array with a defined condition. Then, you need to move the pointer forward or break the iteration. 
    Pointers move along different arrays.
    The most popular problems that can be solved with `One for each` are merging two sorted arrays and 
    checking if one array is a subsequence of another one. 
"""

"""
    ### Merge Sorted Array

    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
    representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
    be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 

    **Example 1:**
    > Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    l, r = m-1, n-1
    for i in reversed(range(len(nums1))):
        if l < 0 or (r >= 0 and nums1[l] < nums2[r]):
            nums1[i] = nums2[r]
            r -= 1
        else:
            nums1[i] = nums1[l]
            l -= 1

"""
    ### Is Subsequence

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting
    some (can be none) of the characters without disturbing the relative positions of the remaining
    characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    **Example 1:**

    > Input: s = "abc", t = "ahbgdc"
    Output: true
"""

def isSubsequence(s: str, t: str) -> bool:
    l = 0
    for r in range(len(t)):
        if l == len(s):
            break
        if s[l] == t[r]:
            l += 1
    return l == len(s)