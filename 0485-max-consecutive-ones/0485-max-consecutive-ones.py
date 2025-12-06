class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = maxCon = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
                if ones > maxCon:
                    maxCon = ones
            else:
                ones = 0
        return maxCon