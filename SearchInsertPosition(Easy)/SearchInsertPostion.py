class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        dummy = 0
        try:
            result = nums.index(target)
            return result
        except (TypeError, ValueError):
            for i in nums:
                if i < target:
                    dummy += 1
                else:
                    return dummy
            return dummy