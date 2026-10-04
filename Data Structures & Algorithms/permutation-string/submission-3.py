class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        one = Counter(s1)
        two = {}
        l = 0

        for r in range(len(s2)):
            two[s2[r]] = 1 + two.get(s2[r], 0)

            if r - l + 1 > len(s1):
                two[s2[l]] -= 1
                if two[s2[l]] == 0:
                    del two[s2[l]]
                l+=1

            
            if one == two:
                return True
        return False