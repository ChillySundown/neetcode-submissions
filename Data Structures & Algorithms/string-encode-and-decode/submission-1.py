class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = str()
        for s in strs:
            enc += str(len(s)) + "#" + s
        return enc
        
    def decode(self, s: str) -> List[str]:
        decryp = list()
        i = 0
        str_len = 0
        print(s)
        while(i < len(s)):
            num_str = str()
            while(s[i] != '#'):
                num_str += s[i]
                i += 1
            i += 1
            print(num_str)
            str_len = int(num_str)
            decryp.append(s[i: i + str_len])
            i += str_len
        return decryp
            
