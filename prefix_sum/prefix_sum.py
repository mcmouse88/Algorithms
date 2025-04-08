"""
    Prefix sum is useful for optimizing computations involving cumulative sums.
    By constructing a prefix sum array we can efficiently answer queries related
    to range sums, subarrays sum and average calculation.
    Approach:
    - Initialize a new array with a length equal to the input array plus one extra
    element, and fill it with zeroes (in some tasks, it's also possible to use a
    single integer variable instead of an array);
    - Iterate through the input array and set the (i + 1)-th element of the prefix
    sum array as the sum of the i-th element of the input array and the i-th element
    of the prefix sum array;
    - To find the sum an of range from the j-th to the i-th element (inclusive) of
    the input array, subtract the (j + 1)-th element of the prefix sum array from
    the i-th element.
    
    Some of the most popular problems that can be solved using `Prefix Sum` included
    - Calculating the sum of a subarray;
    - Counting the number of particular elements in a subarray;
    - Finding the number of subarrays with a given sum;
    - etc.
"""

from typing import List


class NumArray:
    """
    ### 303. Range Sum Query - Immutable

    Given an integer array nums, handle multiple queries of the
    following type:
    Calculate the sum of the elements of nums between indices
    left and right inclusive where left <= right.

    Implement the NumArray class:
    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums
    between indices left and right inclusive
    (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

    **Example 1:**
    > Input
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output
    [null, 1, -1, -3]

    Explanation
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
    """

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = nums[i] + self.prefix[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


def subarraySum(nums: List[int], k: int) -> int:
    """
    ### 560. Subarray Sum Equals K

    Given an array of integers nums and an integer k, return the total number of
    subarrays whose sum equals to k.
    A subarray is a contiguous non-empty sequence of elements within an array.

    **Example 1:**
    > Input: nums = [1,1,1], k = 2
    Output: 2
    """
    res = prefix = 0
    freq = {0: 1}
    for n in nums:
        prefix += n
        if prefix - k in freq:
            res += freq[prefix - k]
        freq[prefix] = freq.get(prefix, 0) + 1
    return res


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    ### 238. Product of Array Except Self

    Given an integer array nums, return an array answer such that answer[i] is equal
    to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
    integer.
    You must write an algorithm that runs in O(n) time and without using the
    division operation.

    **Example 1:**
    > Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    """
    n = len(nums)
    prefix = postfix = 1
    res = [0] * n

    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    for i in reversed(range(n)):
        res[i] *= postfix
        postfix *= nums[i]

    return res
