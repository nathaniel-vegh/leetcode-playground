from collections import defaultdict
nums = [5,7,3,9,4,9,8,3,1]

def largestUniqueNumber(nums):

  res = -1

  counts = defaultdict(int)

  for num in nums:
    counts[num] += 1
  for num, count in counts.items():
    if count == 1:
      res = max(num, res)

  return res

print(largestUniqueNumber(nums))