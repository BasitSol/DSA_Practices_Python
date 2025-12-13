class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        
        for ch in t:
            if ch not in freq:
                return False
            freq[ch]-=1
            if freq[ch] < 0:
                return False

        return True

        ''' if len(s) != len(t):
            return False

        h1 = [0] * 26
        h2 = [0] * 26

        for i in range(len(s)):
            h1[ord(s[i]) - ord('a')]+=1
        for j in range(len(t)):
            h2[ord(t[j]) - ord('a')]+=1
    
        if h1 == h2:
            return True 
        return False '''
        


