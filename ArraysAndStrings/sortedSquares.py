nums = [-4,-1,0,3,10]

def sortedSquares(nums):
  n = len(nums)
  res = [0 for i in range(n)]
  left = 0
  right = n - 1
  for i in range(n-1, -1, -1):
      if abs(nums[left] < nums[right]):
          res[i] = nums[right] ** 2
          right -= 1
      else:
          res[i] = nums[left] ** 2
          left += 1
  return res

print(sortedSquares(nums))