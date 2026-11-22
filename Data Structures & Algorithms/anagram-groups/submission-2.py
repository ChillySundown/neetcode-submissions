class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_to_arr(our_str):
            alpha_arr = [0] * 26
            for c in our_str:
                alpha_index = ord(c) - ord ("a")
                alpha_arr[alpha_index] += 1
            return alpha_arr

        anagram_groups = {}
        for word in strs:
            arr = tuple(convert_to_arr(word))
            if(arr in anagram_groups):
                anagram_groups[arr].append(word)
            else:
                anagram_groups[arr] = [word]
        return list(anagram_groups.values())
        