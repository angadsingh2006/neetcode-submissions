class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nodes = Counter()

        for num in nums:
            nodes[num] +=1

            if nodes[num] > 1:
                return num
            
        return 0


        