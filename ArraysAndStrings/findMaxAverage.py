
nums = [0,1,1,3,3]
k = 4

def findMaxAverage(nums, k):
    
    left = res = curr_sum = 0
    right = k - 1
    for i in range(k):
        curr_sum += nums[i]
    
    res = curr_sum / k
    for i in range(len(nums) - k):
        curr_sum -= nums[left]
        left += 1
        
        right += 1
        curr_sum += nums[right]
        
        res = max(res, curr_sum / k)
        
    return res
            
res = findMaxAverage(nums, k)
print(res)