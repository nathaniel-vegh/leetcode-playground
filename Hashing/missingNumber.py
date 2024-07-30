nums = [0,1,3]

def missingNumber(nums):
  nums_set = set(range(len(nums)+1))
  for i in range(len(nums)):
    if nums[i] in nums_set:
      nums_set.remove(nums[i])

  return nums_set.pop()


print(missingNumber(nums))