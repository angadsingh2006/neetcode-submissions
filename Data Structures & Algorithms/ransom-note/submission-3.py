class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = ""
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)

        for key, value in s2.items():
            if key in s1:
                if value >= s1[key]:
                    res += (key * s1[key])
        ans = Counter(res)

        if s1 == ans:
            return True
        return False