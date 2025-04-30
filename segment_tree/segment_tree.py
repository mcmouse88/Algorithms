from math import ceil, log2
from typing import List


class NumArray:
    """
    ### Range Sum Query - Mutable

    Given an integer array nums, handle multiple queries of the following types:

    Update the value of an element in nums.
    Calculate the sum of the elements of nums between indices left and right
    inclusive where left <= right.

    Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    void update(int index, int val) Updates the value of nums[index] to be val.
    int sumRange(int left, int right) Returns the sum of the elements of nums
    between indices left and right inclusive
    (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

    **Example 1:**
    > Input
    ["NumArray", "sumRange", "update", "sumRange"]
    [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
    [null, 9, null, 8]

    Explanation
    NumArray numArray = new NumArray([1, 3, 5]);
    numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
    numArray.update(1, 2);   // nums = [1, 2, 5]
    numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
    """

    def __init__(self, nums: List[int]):
        height = ceil(log2(self.n))
        tree_size = 2 ** (height+1) - 1
        self.segments = [0] * tree_size
        half = len(self.segments)//2
        self.segments[half:(half+self.n)] = nums
        for i in reversed(range(half)):
            self.segments[i] = self.segments[i*2+1] + self.segments[i*2+2]
        print(self.segments)

    def update(self, index: int, val: int) -> None:
        i = len(self.segments) // 2 + index
        self.segments[i] = val
        while i > 0:
            i = (i-1)//2
            self.segments[i] = self.segments[i*2+1] + self.segments[i*2+2]

    def sumRange(self, left: int, right: int) -> int:
        return self.__sum_range_internal__(left, right, 0, 0, len(self.segments)//2)

    def __sum_range_internal__(self, left, right, i, l, r):
        if r < left or l > right:
            return 0
        if l in range(left, right+1) and r in range(left, right+1):
            return self.segments[i]
        left_res = self.__sum_range_internal__(left, right, i*2+1, l, (l+r)//2)
        right_res = self.__sum_range_internal__(left, right, i*2+2, (l+r)//2+1, r)
        return left_res + right_res
