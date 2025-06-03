"""

"""
from typing import List


def snakesAndLadders(board: List[List[int]]) -> int:
    """
    ### 909. Snakes and Ladders

    You are given an n x n integer matrix board where the cells are labeled from 1
    to n2 in a Boustrophedon style starting from the bottom left of the board
    (i.e. board[n - 1][0]) and alternating direction each row.

    You start on square 1 of the board. In each move, starting from square curr, do
    the following:
        * Choose a destination square next with a label in the range
          [curr + 1, min(curr + 6, n2)].
            * This choice simulates the result of a standard 6-sided die roll: i.e.,
              there are always at most 6 destinations, regardless of the size of the
              board.
        * If next has a snake or ladder, you must move to the destination of that snake
          or ladder. Otherwise, you move to next.
        * The game ends when you reach the square n2.

    A board square on row r and column c has a snake or ladder if board[r][c] != -1.
    The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the
    starting points of any snake or ladder.

    Note that you only take a snake or ladder at most once per dice roll. If the destination
    to a snake or ladder is the start of another snake or ladder, you do not follow the
    subsequent snake or ladder.

    For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination
    square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

    Return the least number of dice rolls required to reach the square n2. If it is not possible
    to reach the square, return -1.

    **Example 1:**
    > Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    Output: 4
    Explanation:
    - In the beginning, you start at square 1 (at row 5, column 0).
    - You decide to move to square 2 and must take the ladder to square 15.
    - You then decide to move to square 17 and must take the snake to square 13.
    - You then decide to move to square 14 and must take the ladder to square 35.
    - You then decide to move to square 36, ending the game.
    - This is the lowest possible number of moves to reach the last square, so return 4.
    """
    pass

def maxCandies(
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        contained_boxes: List[List[int]],
        initial_boxes: List[int]
) -> int:
    """
    ### 1298. Maximum Candies You Can Get from Boxes

    You have n boxes labeled from 0 to n - 1. You are given four arrays: status,
    candies, keys, and containedBoxes where:
    * status[i] is 1 if the ith box is open and 0 if the ith box is closed,
    * candies[i] is the number of candies in the ith box,
    * keys[i] is a list of the labels of the boxes you can open after opening the ith box.
    * containedBoxes[i] is a list of the boxes you found inside the ith box.

    You are given an integer array initialBoxes that contains the labels of the boxes you
    initially have. You can take all the candies in any open box and you can use the keys
    in it to open new boxes and you also can use the boxes you find in it.

    Return the maximum number of candies you can get following the rules above.

    **Example 1:**
    > Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]],
    containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
    Output: 16
    Explanation:
    You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
    Box 1 is closed and you do not have a key for it so you will open box 2. You will
    find 4 candies and a key to box 1 in box 2.
    In box 1, you will find 5 candies and box 3 but you will not find a key to box 3
    so box 3 will remain closed.
    Total number of candies collected = 7 + 4 + 5 = 16 candy.
    """
    pass