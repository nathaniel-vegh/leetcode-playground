def longestOnes(nums, k):
    left = right = res = count = 0
    while(right <= len(nums) - 1):
        if nums[right] == 1:
            right += 1
        
        else:
            count += 1
            right += 1
            
        while count > k:
            if nums[left] == 0:
                count -= 1
            left += 1

                
        res = max(res, right - left + 1)
    return res

res = longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(res)