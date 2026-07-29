class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for num in row:
                if num<0:
                    count = count+1
        return count

  """
1351. Count Negative Numbers in a Sorted Matrix
Solved
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
 

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

  """
