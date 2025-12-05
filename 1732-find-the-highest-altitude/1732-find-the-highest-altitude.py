class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentAlt = maxAlt = 0
        for i in range(len(gain)):
            currentAlt += gain[i]
            if currentAlt > maxAlt:
                maxAlt = currentAlt
        return maxAlt
    
        