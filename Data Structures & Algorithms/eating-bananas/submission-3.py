class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l+r) // 2
            count = 0
            for p in piles:
                hours = math.ceil(p/k)
                count += hours
            if count > h:
                l = k + 1
            elif count <= h:
                res = k
                r = k - 1
        return res
        

