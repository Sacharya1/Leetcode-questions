class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        idx_list = [idx for idx,val in enumerate(nums) if val == 1]

        if len(idx_list) <= 1:
            return len(idx_list)

        result = 1

        for i in range(1, len(idx_list)):
            result *= idx_list[i] - idx_list[i-1]

        return result%(10**9+7)
