class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = [0] * 26

        for char in s:
            index_s = ord(char) - ord('a')
            counter[index_s] += 1

        for char in t:
            index_t = ord(char) - ord('a')
            counter[index_t] -= 1

        for num in counter:
            if num != 0: 
                return False
        
        return True