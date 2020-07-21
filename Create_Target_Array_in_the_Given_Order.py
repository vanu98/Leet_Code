class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i,j in list(zip(nums, index)):
            target.insert(j,i)
        return target
