class Solution(object):
    def jump(self, nums):
        jump = 0
        farthest = 0
        current = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i == current:
                jump +=1
                current = farthest

   
     
           
        return jump        
