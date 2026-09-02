class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        check = set(nums)
        length = 0

        for n in nums:
            count = 0
            if n - 1 not in check:
                curr = n
                count = 1
            
                while curr + 1 in check:
                    count+=1
                    curr+=1
            length = max(count,length)
        return length
            
