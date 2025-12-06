class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        arr = [0] * 101
        for i in nums:
            count += arr[i]
            arr[i]+=1
        return count
    
       
                    
        