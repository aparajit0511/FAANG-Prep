class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()

        if coins[0] > amount and amount != 0:
            return -1

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1,amount+1):

            for coin in coins:

                if coin > i:
                    break 
                else:
                    value = i - coin
                    dp[i] = min(dp[value] + 1,dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()

        if coins[0] > amount and amount != 0:
            return -1
        
        minCoins = float("inf")

        def backtrack(coins,amount,minCoins,combination):
            if amount < 0:
                return minCoins
                
            if amount == 0:
                minCoins = min(minCoins,len(combination))
                
            for coin in coins:
                combination.append(coin)
                minCoins = backtrack(coins,amount-coin,minCoins,combination)
                combination.pop()

            return minCoins
        
        minCoins = backtrack(coins,amount,minCoins,[])

        return minCoins if minCoins != float("inf") else -1