class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = list()
        sort_nums = sorted(nums)
        triples = list()
        taken = set()
        for c in range(1, len(sort_nums) - 1):
            l, r = 0, len(sort_nums) - 1
            while l < c < r:
                three_sum = sort_nums[l] + sort_nums[c] + sort_nums[r]
                if(three_sum < 0):
                    l += 1
                elif(three_sum > 0):
                    r -= 1
                else:
                    combo_tup = (sort_nums[l], sort_nums[c], sort_nums[r]) 
                    if(combo_tup not in taken):
                        triples.append([sort_nums[l], sort_nums[c], sort_nums[r]])
                        taken.add(combo_tup)
                    l += 1
                    r -= 1
        return triples