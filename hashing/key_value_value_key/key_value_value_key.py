"""
    The key-value and value-key pattern is useful when you need to track both key
    and value simultaneously and require constant time access to either.
    In such cases, two hash tables are initialized: one maps keys to values,
    and the other maps values to keys.
"""
import heapq
from collections import defaultdict
from typing import List, Counter
from sortedcontainers import SortedSet


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    ### 347. Top K Frequent Elements

    Given an integer array nums and an integer k, return the k most frequent
    elements. You may return the answer in any order.

    **Example 1:**
    > Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    """
    freq = Counter(nums)
    heap = []
    for key, val in freq.items():
        heapq.heappush(heap, (val, key))
        if len(heap) > k:
            heapq.heappop(heap)
    return [n for _, n in heap]

def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    """
    ### 3160. Find the Number of Distinct Colors Among the Balls

    You are given an integer limit and a 2D array queries of size n x 2.
    There are limit + 1 balls with distinct labels in the range [0, limit].
    Initially, all balls are uncolored. For every query in queries that is of
    the form [x, y], you mark ball x with the color y. After each query, you need
    to find the number of colors among the balls.

    Return an array result of length n, where result[i] denotes the number of colors
    after i-th query.

    Note that when answering a query, lack of a color will not be considered
    as a color.

    **Example 1:**
    > Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
    Output: [1,2,2,3]
    Explanation:
    - After query 0, ball 1 has color 4.
    - After query 1, ball 1 has color 4, and ball 2 has color 5.
    - After query 2, ball 1 has color 3, and ball 2 has color 5.
    - After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
    """
    balls, colors = {}, defaultdict(int)
    res = [0] * len(queries)

    for i, (ball, color) in enumerate(queries):
        if ball in balls:
            clr = balls[ball]
            colors[clr] -= 1
            if colors[clr] == 0:
                colors.pop(clr)
        balls[ball] = color
        colors[color] += 1
        res[i] = len(colors)
    return res


class NumberContainers:
    """
    ### 2349. Design a Number Container System

    Design a number container system that can do the following:
    - Insert or Replace a number at the given index in the system.
    - Return the smallest index for the given number in the system.

    Implement the NumberContainers class:
    - NumberContainers() Initializes the number container system.
    - void change(int index, int number) Fills the container at index with the
      number. If there is already a number at that index, replace it.
    - int find(int number) Returns the smallest index for the given number,
      or -1 if there is no index that is filled by number in the system.

    **Example 1:**
    > Input:
    ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
    [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
    Output:
    [null, -1, null, null, null, null, 1, null, 2]
    Explanation:
    NumberContainers nc = new NumberContainers();
    nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
    nc.change(2, 10); // Your container at index 2 will be filled with number 10.
    nc.change(1, 10); // Your container at index 1 will be filled with number 10.
    nc.change(3, 10); // Your container at index 3 will be filled with number 10.
    nc.change(5, 10); // Your container at index 5 will be filled with number 10.
    nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest
    index that is filled with 10 is 1, we return 1.
    nc.change(1, 20); // Your container at index 1 will be filled with number 20.
    Note that index 1 was filled with 10 and then replaced with 20.
    nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index
    that is filled with 10 is 2. Therefore, we return 2.
    """
    def __init__(self):
        self.indices = {}
        self.nums = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.indices[index] = number
        heapq.heappush(self.nums[number], index)

    def find(self, number: int) -> int:
        heap = self.nums[number]
        while heap and self.indices[heap[0]] != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1
