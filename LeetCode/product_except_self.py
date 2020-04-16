class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums),[1] * len(nums)
        
        for i in range(1,len(nums)):
            left[i]*=nums[i-1]*left[i-1]
            
        for i in range(len(nums)-2,-1,-1):
            right[i]*=nums[i+1]*right[i+1]
        
        return [l*r for l,r in zip(left,right)]
