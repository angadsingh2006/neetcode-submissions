class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        string = "".join(str(d) for d in digits)
        new = int(string)
        new += 1

        res = [int(d) for d in str(new)]

        return res