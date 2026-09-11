class Solution(object):
    def uniqueOccurrences(self, arr):
        map = {}
        n = len(arr)
        for i in range (0,n):
            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
        occurence = []
        for value in map.values():
            if value in occurence :
                return False
            occurence.append(value)
        return True

  """
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
 

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
  """
