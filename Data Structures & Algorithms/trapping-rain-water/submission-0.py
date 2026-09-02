class Solution:
    def trap(self, height: List[int]) -> int:
        # def findWater(i, j):
        #     total_area = (j - i - 1) * min(height[j], height[i])
        #     for k in range(i+1, j):
        #         total_area -=  height[k]
        #     return total_area
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        def findWater(i):
            return max(min(maxLeft[i], maxRight[i]) - height[i], 0)

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
        totalWater = 0
        for i in range(len(height)):
            totalWater += findWater(i)
        return totalWater
