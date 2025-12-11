class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                #swap(nums[current],nums[lastNonZero])
                nums[current], nums[lastNonZero] = nums[lastNonZero], nums[current]
                lastNonZero+=1
            


        

       

        