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
        raise NotImplementedError("Not yet implement")

    def update(self, index: int, val: int) -> None:
        raise NotImplementedError("Not yet implement")

    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError("Not yet implement")