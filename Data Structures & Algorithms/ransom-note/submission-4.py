class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = ""
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)

        for key, value in s1.items():
            if s2[key] < value:
                return False
        return True