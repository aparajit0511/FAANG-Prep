class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxProfit = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                maxProfit = max(maxProfit,nums[j]-nums[i])

        return maxProfit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        left = 0

        for right in range(1,len(prices)):

            if prices[left] >= prices[right]:
                left = right

            maxProfit = max(maxProfit,prices[right]-prices[left])

        return maxProfit


