class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2*n)
        idx = 0
        for i in range(n):
            ans[idx] = nums[i]
            idx += 1
            ans[idx] = nums[i+n]
            idx += 1
        return ans

        