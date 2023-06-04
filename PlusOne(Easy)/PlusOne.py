class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        word = ""
        final = []
        for i in digits:
            word = word + str(i)
        result = int(word) + 1
        for i in str(result):
            final.append(int(i))
        return final