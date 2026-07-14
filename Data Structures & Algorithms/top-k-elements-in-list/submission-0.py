class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Make hashmap
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq_map[n] += 1
            else:
                freq_map[n] = 1
        
        ord_map = {k: v for k, v in sorted(freq_map.items(), key=lambda item : item[1], reverse=True)}

        return list(ord_map.keys())[0:k]