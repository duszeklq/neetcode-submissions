class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        set_s = [0] * 26 
        set_t = [0] * 26 

        for char in s:
            index = ord(char) - ord('a')
            set_s[index] +=1

        for char in t:
            index = ord(char) - ord('a')
            set_t[index] +=1

        return set_s == set_t