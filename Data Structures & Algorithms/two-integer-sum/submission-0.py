class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder_map = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if nums[i] in remainder_map:
                key = nums[i]
                return [remainder_map[key], i];
            else:
                remainder_map[rem] = i
            print(remainder_map)
        

            