"""
    Prefix sum is useful for optimizing computations involving cumulative sums.
    By constructing a prefix sum array we can efficiently answer queries related
    to range sums, subarrays sum and average calculation.
    Approach:
    - Initialize a new array with a length equal to the input array plus one extra
    element, and fill it with zeroes (in some tasks, it's also possible to use a
    single integer variable instead of an array);
    - Iterate throught the input array and set the (i + 1)-th element of the prefix
    sum array as the sum of the i-th element of the input array and the i-th element
    of the prefix sum array;
    - To find the sum a of range from the j-th to the i-th element (inclusive) of
    the input array, substract the (j + 1)-th element of the prefix sum array from
    the i-th element.
    
    Some of the most popular problems that can be solved using `Prefix Sum` included
    - Calculating the sum of a subarray;
    - Counting the number of particular elements in a subarray;
    - Finding the number of subarrays with a given sum;
    - etc.
"""

from collections import defaultdict
from typing import List
from math import ceil

class NumArray:
    """
    ### Range Sum Query - Immutable

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
            self.prefix[i+1] = nums[i] + self.prefix[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
                