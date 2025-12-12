class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel = set(jewels)
        for i in range(len(stones)):
            if stones[i] in jewel:
                count+=1
        return count

        