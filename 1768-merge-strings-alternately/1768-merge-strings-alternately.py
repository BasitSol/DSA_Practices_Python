class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i, j = 0, 0
        w1 = len(word1)
        w2 = len(word2)

        while i < w1 and j < w2:
            ans.append(word1[i])
            ans.append(word2[j])
            i+=1
            j+=1
        
        if i < w1:
            ans.extend(word1[i:])
            i+=1
        if j < w2:
            ans.extend(word2[j:])
            j+=1
        
        return "".join(ans)
        