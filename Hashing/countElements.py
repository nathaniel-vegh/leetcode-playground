nums = [1,2,3]

def countElements(nums):
  count = 0
  nums_set = set(nums)
  for i in range(len(nums)):
    if nums[i] + 1 in nums_set:
      count += 1
  return count

print(countElements(nums))