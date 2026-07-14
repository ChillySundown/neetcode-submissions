class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toAnagram(s):
            ana_map = {}
            for char in s:
                if char in ana_map:
                    ana_map[char] += 1
                else:
                    ana_map[char] = 1
            return ana_map

        ana_groups = []
        for s in strs:
            if not ana_groups:
                ana_groups.append([s]);
            else:
                grouped = False
                for group in ana_groups:
                   if toAnagram(group[-1]) == toAnagram(s):
                        grouped = True
                        group.append(s)
                if not grouped:
                    ana_groups.append([s])
        return ana_groups