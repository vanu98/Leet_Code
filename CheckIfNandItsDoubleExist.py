class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr1 = [str(i) for i in arr]
        for i in arr:
            if str(i*2) in arr1:
                if i==0: 
                    if arr.count(0)>1: return 1
                    else: continue
                else: return 1
        return 0
