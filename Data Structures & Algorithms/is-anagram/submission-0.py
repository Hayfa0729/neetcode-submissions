class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        if len(s) != len(t):
            return False
        for i in range (len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        for i in range(len(t)):
            if t[i] not in hash_map:
                return False
            else:
                hash_map[t[i]] -= 1
        for count in hash_map.values():
            if count != 0:
                return False
        return True


        