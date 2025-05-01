"""

"""
from typing import List


def matchPlayersAndTrainers(players: List[int], trainers: List[int]) -> int:
    """
    ### 2410. Maximum Matching of Players With Trainers

    You are given a 0-indexed integer array players, where players[i] represents
    the ability of the ith player. You are also given a 0-indexed integer array
    trainers, where trainers[j] represents the training capacity of the jth trainer.

    The ith player can match with the jth trainer if the player's ability is less
    than or equal to the trainer's training capacity. Additionally, the ith player
    can be matched with at most one trainer, and the jth trainer can be matched with
    at most one player.

    Return the maximum number of matchings between players and trainers that satisfy
    these conditions.

    **Example 1:**
    > Input: players = [4,7,9], trainers = [8,2,5,8]
    Output: 2
    Explanation:
    One of the ways we can form two matchings is as follows:
    - players[0] can be matched with trainers[0] since 4 <= 8.
    - players[1] can be matched with trainers[3] since 7 <= 8.
    It can be proven that 2 is the maximum number of matchings that can be formed.
    """
    pass

def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    """
    ### 1007. Minimum Domino Rotations For Equal Row

    In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves
    of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on
    each half of the tile.)
    We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
    Return the minimum number of rotations so that all the values in tops are the
    same, or all the values in bottoms are the same.
    If it cannot be done, return -1.

    **Example 1:**
    > Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
    Output: 2
    Explanation:
    The first figure represents the dominoes as given by tops and bottoms: before
    we do any rotations. If we rotate the second and fourth dominoes, we can make
    every value in the top row equal to 2, as indicated by the second figure.
    """
    pass