class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        i = count = 0 
        j = len(nums) -1

        while i <= j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
            elif nums[i] > nums[j]:
                j -= 1
                nums[j] += nums[j+1]
                count +=1 
            else:
                i += 1
                nums[i] += nums[i-1]
                count +=1 
        return count
