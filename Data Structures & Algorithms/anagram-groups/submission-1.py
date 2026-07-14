class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            alpha_arr = 26 * [0];
            for c in s:
                alpha_arr[ord(c) - ord("a")] += 1
            alpha_key = tuple(alpha_arr)
            if alpha_key in groups:
                groups[alpha_key].append(s)
            else:
                groups[alpha_key] = [s]
        return list(groups.values())