class Solution:
  def largest(self, n:int, arr : List[int]) -> int:
    max = arr[0]
    for i range(1,n):
        if arr[i] > max:
          max = arr[i]
      return max
