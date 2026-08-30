class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        greatest_count = 0
        for n in num_set:
            if (n-1) not in num_set: #start of seq
                current_count = 1
                while (n + current_count) in num_set:
                    current_count += 1
                if current_count > greatest_count:
                    greatest_count = current_count
        return greatest_count