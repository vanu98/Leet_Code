class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            if nums[i]+nums[i+1]==target:
                return [i,i+1]
            
