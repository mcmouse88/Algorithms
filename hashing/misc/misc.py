"""
    There are various kinds of problems that can be solved using a data structure
    based on a hash table.
    Hashing involves the process of mapping inputs, known as keys, to outputs,
    also known as values, through the use of a hash function, which is based on
    a mathematical algorithm. It allows reducing the time complexity of searching from
    O(n) to O(1) compared to an array.
    Hash tables are essentially organized arrays. Therefore, at each index or
    bucket, only one value can exist. Thus, when more than one key results in
    the same hash function output, a collision occurs.
    The ways to calculate hash function:
        * Division method - hash = key % k where k is a chosen integer, often
          a size of an array
        * Multiplication method - hash = floor(m * (key * a % 1)) where 0 <= A < 1,
          m is the desired size of the hash table

    A collision occurs when two or more keys have the same hash function result and
    thus, are allocated to the same bucket.
    There are typically two ways of handling collisions - open addressing and separate
    chaining.

    In open addressing, elements are always stored in the hash table itself unlike
    in separate chaining. To handle collisions while keeping the elements contained
    within the table, probing and rehashing are used.

    * Linear probing is the technique of searching for the next available bucket
    whenever a collision is detected - hash = (key % k) + i. This function applies
    until it finds an empty bucket

    * Quadratic probing is similar to linear probing and when new indices are
    decided with quadratic methods such as this - hash = (key % k) + i^2.
    When a collision occurs, the key searches at the i^2 index from the collision
    index until it finds an appropriate index.

    * Double hashing is using another secondary hashing function. If the second
    hashing function leads to a filled bucket, then it is applied again until an
    empty bucket is found.

    Separate chaining is another common approach to dealing with collisions.
    Separate chaining involves storing a linked list in each bucket of the hash
    table. When a collision occurs, the hash table just adds the key-value pair
    to the linked list in the corresponding bucket.
"""
from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    ### 49. Group Anagrams

    Given an array of strings strs, group the together. You can return the answer
    in any order.

    **Example 1:**
    > Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Explanation:
    * There is no string in strs that can be rearranged to form "bat".
    * The strings "nat" and "tan" are anagrams as they can be rearranged to form
    each other.
    * The strings "ate", "eat", and "tea" are anagrams as they can be rearranged
    to form each other.
    """
    res = defaultdict(list)
    for word in strs:
        curr = [0] * 26
        for ch in word:
            curr[ord(ch) - ord('a')] += 1
        key = "".join(chr(n) for n in curr)
        res[key].append(word)
    return list(res.values())


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
    prefix = res = 0
    map_sum = {0: 1}
    for n in nums:
        prefix += n
        if prefix - k in map_sum:
            res += map_sum[prefix - k]
        map_sum[prefix] = map_sum.get(prefix, 0) + 1
    return res


def longestConsecutive(nums: List[int]) -> int:
    """
    ### 128. Longest Consecutive Sequence

    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.

    **Example 1:**
    > Input: Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
    Therefore its length is 4.
    """
    nums = set(nums)
    res = 0
    for num in nums:
        if num - 1 in nums:
            continue
        cnt = 1
        next_num = num + 1
        while next_num in nums:
            cnt += 1
            next_num += 1
        res = max(cnt, res)
    return res