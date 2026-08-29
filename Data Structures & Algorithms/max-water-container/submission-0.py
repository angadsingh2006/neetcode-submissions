class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1 
        maxx = 0
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            volume = height*width

            maxx = max(volume,maxx)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return maxx



            
