"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

e.g
Input: nums = [-3,2,-3,4,2]
Output: 5

Input: nums = [1,-2,-3]
Output: 5

"""

def minStartValue(nums):
  ans = 1
  prefix = [nums[0]]
  for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[i-1])

  while True:
    prefix_plus_ans = [pre + ans for pre in prefix]
    if not False in [pre >= 1 for pre in prefix_plus_ans]:
      return ans
    else:
      ans += 1

nums = [1,2]

res = minStartValue(nums)
print(res)