class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        n = len(nums)
        ans = [0] * n

        less_count = 0

        for num in nums:
            if num < pivot:
                less_count += 1
        
        left = 0
        mid = less_count
        for num in nums:
            if num < pivot:
                ans[left] = num
                left += 1
            elif num == pivot:
                ans[mid] = num
                mid+=1
        right = mid 
        for num in nums:
            if num > pivot:
                ans[right] = num
                right += 1
                
        return ans
        