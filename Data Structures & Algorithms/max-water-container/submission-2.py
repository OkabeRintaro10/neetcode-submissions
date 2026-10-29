class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        area = 0
        while lp < rp:
            curr_area = (rp - lp) * min(heights[rp], heights[lp])
            print(curr_area)
            area = max(area, curr_area)

            if heights[lp] < heights[rp]:
                lp +=1
            else:
                rp -=1
        return area
