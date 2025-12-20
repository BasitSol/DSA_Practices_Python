class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1 = set(nums1)
        l2 = set(nums2)
        ans1 = []
        ans2 = []

        for i in l1:
            if i not in l2:
                ans1.append(i)

        for j in l2:
            if j not in l1:
                ans2.append(j)
        return ans1, ans2

        