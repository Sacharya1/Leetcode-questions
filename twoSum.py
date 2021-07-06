#1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict=dict()      
        for i in range(len(nums)):
            if (target-nums[i]) in myDict:
                return [myDict[(target-nums[i])],i]
            else:
                myDict[nums[i]]=i
