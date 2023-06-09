class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dummy = []
        for i in nums:
            if i not in dummy:
                dummy.append(i)
            else:
                dummy.remove(i)
        return dummy[0]