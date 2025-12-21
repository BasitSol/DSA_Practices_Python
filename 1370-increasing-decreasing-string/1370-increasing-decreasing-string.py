class Solution:
    def sortString(self, s: str) -> str:
        n = len(s)
        freq = {}
        order = 0
        ans = []

        for char in s: 
            freq[char] = freq.get(char, 0) + 1
        
        while n > len(ans):
            if order % 2 == 0:
                for i in range(26):
                    char_key = chr(i + ord('a'))
                    if freq.get(char_key, 0) != 0:
                        ans.append(char_key)
                        freq[char_key]-=1
                order += 1
                
            else:
                for i in range(25, -1, -1):
                    char_key = chr(i + ord('a'))
                    if freq.get(char_key, 0) != 0:
                        ans.append(char_key)
                        freq[char_key]-=1
                order += 1
        
        return "".join(ans)



        