class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        alpha = set(sentence.lower())
        return len(alpha) == 26

        