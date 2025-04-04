"""
    Sliding window with fixed side is useful when you need to perform operations 
    on k contiguous elements in a structure (such as an array, string, etc.).
    An advantage of this algorithm is that it allows you to traverse the structure
    only once while maintaining a fixed window size.
    This approach reduces the time complexity to O(n), making it particularly
    effective for large dataset.
    
    Some of the most popular problems that can be solved with `Fixed size sliding window`
    include finding maximum (sum, xor, etc.) on k contiguous elements in an array. 
"""

from typing import List

def find_max_average(nums: List[int], k: int) -> float:
    """
    ### Maximum Average Subarray I

    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average 
    value and return this value. Any answer with a calculation error less than 10-5 will
    be accepted.
 

    **Example 1:**
    > Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    """
    acc = sum(nums[:k])
    res, l = acc, 0
    for r in range(k, len(nums)):
        acc += nums[r] - nums[l]
        res = max(res, acc)
        l += 1           
            
    return res / k

def max_vowels(s: str, k: int) -> int:
    """
    ### Maximum Number of Vowels in a Substring of Given Length

    Given a string s and an integer k, return the maximum number of vowel letters in any
    substring of s with length k.
    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 

    **Example 1:**
    > Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = res = 0
    l = 0
    for r in range(len(s)):
        if r - l + 1 > k:
            if s[l] in vowels:
                count -= 1
            l += 1
            
        if s[r] in vowels:
            count += 1
        res = max(res, count)
                
    return res

def get_averages(nums: List[int], k: int) -> List[int]:
    """
    ### K Radius Subarray Averages

    You are given a 0-indexed array nums of n integers, and an integer k.
    The k-radius average for a subarray of nums centered at some index i with the radius
    k is the average of all elements in nums between the indices i - k and i + k (inclusive).
    If there are less than k elements before or after the index i, then the k-radius average is -1.
    Build and return an array avgs of length n where avgs[i] is the k-radius average for the
    subarray centered at index i.

    The average of x elements is the sum of the x elements divided by x, using integer division.
    The integer division truncates toward zero, which means losing its fractional part.

    For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75,
    which truncates to 2. 

    **Example 1:**
    > Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
    Output: [-1,-1,-1,5,4,4,-1,-1,-1]
    Explanation:
    - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
    - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
    Using integer division, avg[3] = 37 / 7 = 5.
    - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
    - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
    - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
    """
    res = [-1] * len(nums)
    curr = l = 0
    window = k * 2 + 1
    for r in range(len(nums)):
        curr += nums[r]
        if r - l + 1 < window:
            continue
        res[(l + r) // 2] = curr // window
        curr -= nums[l]
        l += 1
    return res
