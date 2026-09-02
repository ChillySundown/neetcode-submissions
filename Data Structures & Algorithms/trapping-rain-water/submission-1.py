class Solution:
    def trap(self, height: List[int]) -> int:
        # def findWater(i, j):
        #     total_area = (j - i - 1) * min(height[j], height[i])
        #     for k in range(i+1, j):
        #         total_area -=  height[k]
        #     return total_area
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        def findMaxBarriers():
            #find maxLeft
            currentMax = 0
            for i in range(len(height)):
                maxLeft[i] = currentMax
                currentMax = max(height[i], currentMax)
            
            currentMax = 0
            for j in range(len(height)-1, 0, -1):
                maxRight[j] = currentMax
                currentMax = max(height[j], currentMax)

        findMaxBarriers()
        mins = [min(l, r) for l, r in zip(maxLeft, maxRight)]
        totalWater = 0
        for i in range(len(height)):
            totalWater += max(mins[i] - height[i], 0)
        return totalWater
