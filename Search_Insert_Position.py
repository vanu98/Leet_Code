class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i==target:
                present = True
                index = nums.index(i)
                break
            else:
                present = False

        if present==True:
	        return index
        else:
            for i in nums:
                if(i>target):
                    return nums.index(i)
                else:
                    continue
            return len(nums)
