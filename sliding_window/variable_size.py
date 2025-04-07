"""
    Sliding window with variable size is useful when you need to find subset 
    with predefined condition.

    In a variable window problem,the window size is not fixed and can change
    dynamically based on certain conditions or criteria. The template for 
    solving a variable window problem involves maintaining two pointers, start
    and end, which represent the indices of the current window.

    Initialize the window indices: Start by initializing the start and end
    pointers to the first element of the sequence or array.

    Expand the window: Check a condition to determine whether to expand the window.
    If the condition is satisfied, increment the end pointer to expand the window size.

    Process the window: Once the window size meets the desired criteria or condition,
    perform the required computations or operations on the elements within the window.

    Adjust the window size: If the window size exceeds the desired criteria, adjust
    the window by moving the start pointer. Iterate or loop until the window size matches
    the desired criteria, and update the window accordingly.
"""

from typing import List

def length_of_longest_substring(s: str) -> int:
    """
    ### Longest Substring Without Repeating Characters

    Given a string s, find the length of the longest without duplicate characters.
 
    **Example 1:**
    > Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    """
    used = set()
    res = l = 0
    for ch in s:
        while ch in used:
            used.remove(s[l])
            l += 1
        used.add(ch)
        res = max(res, len(used))
    return res

def min_subarray_len(target: int, nums: List[int]) -> int:
    """
    ### Minimum Size Subarray Sum

    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a whose sum is greater than or equal to target.
    If there is no such subarray, return 0 instead.
 
    **Example 1:**
    > Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    """
    l = curr = 0
    res = float("inf")
    for r, n in enumerate(nums):
        curr += n
        while curr >= target:
            res = min(res, r - l + 1)
            curr -= nums[l]
            l += 1
    return 0 if res == float("inf") else res

def longestOnes(nums: List[int], k: int) -> int:
    """
    ### Max Consecutive Ones III

    Given a binary array nums and an integer k, return the maximum number of consecutive
    1's in the array if you can flip at most k 0's.
 
    **Example 1:**
    > Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    """
    res = l = 0
    zerocount = 0
    for r, n in enumerate(nums):
        zerocount += 0 if n else 1
        while zerocount > k:
            zerocount -= 0 if nums[l] else 1
            l += 1
        res = max(res, r - l + 1)
    return res
