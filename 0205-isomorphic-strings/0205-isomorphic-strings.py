class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_to_t = {}
        used_t = set()

        for i in range(len(s)):
            
            c1 = s[i]
            c2 = t[i]

            if c1 in s_to_t: 
                if s_to_t[c1] != c2:
                    return False
            else:
                if c2 in used_t:
                    return False
                s_to_t[c1] = c2
                used_t.add(c2)
        return True



        




