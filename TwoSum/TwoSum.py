class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = dict()

        for i in range(len(nums)) :
            num = nums[i]
            number = target - num

            if num in map_dict:
                return[map_dict[num], i]
            else:
                map_dict[number] = i