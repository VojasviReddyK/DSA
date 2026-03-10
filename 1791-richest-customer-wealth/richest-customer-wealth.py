class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            current_wealth = sum(customer)
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth

obj=Solution()
print(obj.maximumWealth([[1,2,3], [5,7,4]]))
        