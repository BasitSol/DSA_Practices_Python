class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = s + s
        # Remove first and last character
        modified = doubled[1:-1]
        # Check if original string exists in this modified string
        return s in modified
        
    '''
    class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for k in range(1, n // 2 + 1):
            if n % k != 0:
                continue

            pattern = s[:k]
            is_repeated = True

            for i in range(k, n, k):
                if s[i:i + k] != pattern:
                    is_repeated = False
                    break

            if is_repeated:
                return True

        return False

    '''