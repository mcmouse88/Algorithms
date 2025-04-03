from typing import List

"""
    The opposite directions approach is useful when checking elements from both the start and the end
    of an array. In that case, the pointers move toward each other.
"""

"""
### Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

**Example 1:**

> Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

"""
### Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same
element twice.

Your solution must use only constant extra space.

**Example 1:**

> Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""
def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < r:
        add = numbers[l] + numbers[r]
        if add == target:
            return [l+1, r+1]
        if add > target:
            r -= 1
        else:
            l += 1