class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = (l+r) // 2
            hours = 0

            for pile in piles:
                count = math.ceil(pile/k)
                hours += count
            
            if hours > h:
                l = k + 1
            elif hours <= h:
                res = k
                r = k - 1
        return res
            

