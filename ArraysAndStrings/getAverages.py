def getAverages(nums, k):
  length = len(nums)
  prefix = [nums[0]]
  for i in range(1, length):
    prefix.append(nums[i] + prefix[i-1])

  res = [-1 for num in nums]
  for i in range(length-k):
    if i >= k:
      subarr_sum = prefix[i+k] - prefix[i-k] + nums[i-k]
      subarr_avg = int(subarr_sum / (2*k + 1))
      res[i] = subarr_avg
    else:
      continue

  return res


nums = [7,4,3,9,1,8,5,2,6]
k = 3
res = getAverages(nums, k)
print(res)
