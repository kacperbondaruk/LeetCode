class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arrays = set()
        fNumber = 0
        output = 0

        for i in range(len(s)):
            while s[i] in arrays:
                arrays.remove(s[fNumber])
                fNumber += 1
            arrays.add(s[i])
            output = max(output, i - fNumber + 1)
        return output