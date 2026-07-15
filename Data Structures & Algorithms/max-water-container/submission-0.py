class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        ans = 0
        while l<r:
            vol =  (r-l)*min(height[l],height[r])

            ans = max(ans,vol)

            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        
        return ans

        