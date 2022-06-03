// time = O(n)
// space = O(1)

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0, low = INT_MAX;
        for (auto &price: prices) {
            if (price < low) low = price;
            if (price - low > max_profit) max_profit = price - low;
        }
        return max_profit;
    }
};