"""

"""
from typing import Counter, List


def isAnagram(s: str, t: str) -> bool:
    """
    ### 242. Valid Anagram

    Given two strings s and t, return true if t is an of s, and false otherwise.

    **Example 1:**
    > Input: s = "anagram", t = "nagaram"
    Output: true
    """
    freq = Counter(s)
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            freq.pop(ch)
    return len(freq) == 0


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    ### 350. Intersection of Two Arrays II

    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays,
    and you may return the result in any order.

    **Example 1:**
    > Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]
    """
    freq = Counter(nums1)
    res = []
    for n in nums2:
        if n in freq and freq[n] > 0:
            res.append(n)
            freq[n] -= 1
    return res


def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    """
    ### 1128. Number of Equivalent Domino Pairs

    Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d]
    if and only if either (a == c and b == d), or (a == d and b == c) - that is,
    one domino can be rotated to be equal to another domino.
    Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
    and dominoes[i] is equivalent to dominoes[j].

    **Example 1:**
    > Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1
    """
    freq = Counter(tuple(sorted(dom)) for dom in dominoes)
    res = 0
    for cnt in freq.values():
        res += cnt * (cnt - 1) // 2
    return res
