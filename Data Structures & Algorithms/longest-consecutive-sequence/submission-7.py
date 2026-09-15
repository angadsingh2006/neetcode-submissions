class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        res = 0

        for num in nums:
            count = 0
            if num - 1 not in seen:
                curr = num
                count = 1

                while curr + 1 in seen:
                    curr +=1
                    count +=1
                
            res = max(res, count)
        return res
                