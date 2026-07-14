class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def convert_to_hashmap(string):
            hashmap = {}
            for char in string:
                if char in hashmap:
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
            return hashmap

        map1 = convert_to_hashmap(s)
        map2 = convert_to_hashmap(t)

        return map1 == map2