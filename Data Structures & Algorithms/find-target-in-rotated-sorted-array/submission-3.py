class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            while l <= m:
                if nums[l] != target:
                    l+=1
                else:
                    return l

            while m <= r:
                if nums[m] != target:
                    m+=1
                else:
                    return m
        return -1