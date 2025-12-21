class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        char_freq = {}

        for ch in chars:
            char_freq[ch] = char_freq.get(ch, 0) + 1
        
        total_length = 0

        for word in words:
            word_freq = {}
            valid = True

            for ch in word:
                word_freq[ch] = word_freq.get(ch, 0) + 1
                if word_freq.get(ch,0) > char_freq.get(ch, 0):
                    valid = False
                    break

            if valid:
                total_length += len(word)
        
        return total_length
 