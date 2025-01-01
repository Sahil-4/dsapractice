#include <iostream>
#include <vector>

using namespace std;

class Solution1 {
private:
    int recursion(vector<int>& prices, int N, int index, int cap, int hold) {
        if (index == N || cap == 0) return 0;

        int profit = 0;

        if (!hold) {
            // buy or dont buy 
            int buy = -prices[index] + recursion(prices, N, index+1, cap, 1);
            int not_buy = recursion(prices, N, index+1, cap, 0);
            profit = max(buy, not_buy);
        } else {
            // sell or dont sell 
            int sell = +prices[index] + recursion(prices, N, index+1, cap-1, 0);
            int not_sell = recursion(prices, N, index+1, cap, 1);
            profit = max(sell, not_sell);
        }

        return profit;

        // Complexity analysis 
        // Time : O(2^(N+k)) 
        // Space : O(N+k) 
    }

    int memoization(vector<int>& prices, int N, int index, int cap, int hold, vector<vector<vector<int>>> &dp) {
        if (index == N || cap == 0) return 0;

        if (dp[index][cap][hold] != -1) return dp[index][cap][hold];

        int profit = 0;

        if (!hold) {
            // buy or dont buy 
            int buy = -prices[index] + memoization(prices, N, index+1, cap, 1, dp);
            int not_buy = memoization(prices, N, index+1, cap, 0, dp);
            profit = max(buy, not_buy);
        } else {
            // sell or dont sell 
            int sell = +prices[index] + memoization(prices, N, index+1, cap-1, 0, dp);
            int not_sell = memoization(prices, N, index+1, cap, 1, dp);
            profit = max(sell, not_sell);
        }

        return dp[index][cap][hold] = profit;

        // Complexity analysis 
        // Time : O(2*(N+k)) 
        // Space : O(N+k) + O(N*(k+1)*2) for memory 
    }

    int tabulation(vector<int>& prices, int N, int k) {
        vector<vector<vector<int>>> dp(N+1, vector<vector<int>>(k+1, vector<int>(2, 0)));

        // base case - handled by init 

        // recurrence 
        for (int index = N-1; index >= 0; index--) {
            for (int cap = 1; cap <= k; cap++) {
                for (int hold = 0; hold <= 1; hold++) {
                    int profit = 0;

                    if (!hold) {
                        // buy or dont buy 
                        int buy = -prices[index] + dp[index+1][cap][1];
                        int not_buy = dp[index+1][cap][0];
                        profit = max(buy, not_buy);
                    } else {
                        // sell or dont sell 
                        int sell = +prices[index] + dp[index+1][cap-1][0];
                        int not_sell = dp[index+1][cap][1];
                        profit = max(sell, not_sell);
                    }

                    dp[index][cap][hold] = profit;
                }
            }
        }

        // return 
        return dp[0][k][0];

        // Complexity analysis 
        // Time : O(N*k*2) 
        // Space : O((N+1)*(k+1)*2) for memory 
    }

    int optimise(vector<int>& prices, int N, int k) {
        vector<vector<int>> dpn(k+1, vector<int>(2, 0));

        // base case - handled by init 

        // recurrence 
        for (int index = N-1; index >= 0; index--) {
            vector<vector<int>> dpc(k+1, vector<int>(2, 0));

            for (int cap = 1; cap <= k; cap++) {
                // buy or dont buy 
                int buy = -prices[index] + dpn[cap][1];
                int not_buy = dpn[cap][0];
                int b_profit = max(buy, not_buy);

                // sell or dont sell 
                int sell = +prices[index] + dpn[cap-1][0];
                int not_sell = dpn[cap][1];
                int s_profit = max(sell, not_sell);

                dpc[cap][0] = b_profit;
                dpc[cap][1] = s_profit;
            }

            dpn = dpc;
        }

        // return 
        return dpn[k][0];

        // Complexity analysis 
        // Time : O(N*k) 
        // Space : O(2*(k+1)*2) for memory 
    }

public:
    int maxProfit(int k, vector<int>& prices) {
        int N = prices.size();

        // recursion 
        // return recursion(prices, N, 0, k, 0);

        // memoization 
        // vector<vector<vector<int>>> dp(N, vector<vector<int>>(k+1, vector<int>(2, -1)));
        // return memoization(prices, N, 0, k, 0, dp);

        // tabulation 
        // return tabulation(prices, N, k);

        // optimise 
        return optimise(prices, N, k);
    }
};

void p1() {
    // Problem 1 : Leetcode 188. Best Time to Buy and Sell Stock IV - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-profit4657/1 

    int k = 2;
    vector<int> prices = {10, 22, 5, 75, 65, 80};

    int profit = Solution1().maxProfit(k, prices);
    cout << profit << endl;
}

class Solution2 {
private:
    int recursion(vector<int>& prices, int N, int index, int hold) {
        if (index >= N) return 0;

        int profit = 0;

        if (!hold) {
            // buy or dont buy 
            int buy = -prices[index] + recursion(prices, N, index+1, 1);
            int not_buy = recursion(prices, N, index+1, 0);
            profit = max(buy, not_buy);
        } else {
            // sell or dont sell 
            int sell = +prices[index] + recursion(prices, N, index+2, 0);
            int not_sell = recursion(prices, N, index+1, 1);
            profit = max(sell, not_sell);
        }

        return profit;

        // Complexity analysis 
        // Time : O(2^(N*2)) 
        // Space : O(2*N) stack space 
    }

    int memoization(vector<int>& prices, int N, int index, int hold, vector<vector<int>> &dp) {
        if (index >= N) return 0;

        if (dp[index][hold] != -1) return dp[index][hold];

        int profit = 0;

        if (!hold) {
            // buy or dont buy 
            int buy = -prices[index] + memoization(prices, N, index+1, 1, dp);
            int not_buy = memoization(prices, N, index+1, 0, dp);
            profit = max(buy, not_buy);
        } else {
            // sell or dont sell 
            int sell = +prices[index] + memoization(prices, N, index+2, 0, dp);
            int not_sell = memoization(prices, N, index+1, 1, dp);
            profit = max(sell, not_sell);
        }

        return dp[index][hold] = profit;

        // Complexity analysis 
        // Time : O(2*(N*2)) 
        // Space : O(2*N) stack space + O(N*2) for memory 
    }

    int getDP(vector<vector<int>> &dp, int index, int hold) {
        if (index < 0 || index >= dp.size()) return 0;
        return dp[index][hold];
    }

    int tabulation(vector<int>& prices, int N) {
        vector<vector<int>> dp(N, vector<int>(2, 0));

        for (int index = N-1; index >= 0; index--) {
            for (int hold = 0; hold <= 1; hold++) {
                int profit = 0;

                if (!hold) {
                    // buy or dont buy 
                    int buy = -prices[index] + getDP(dp, index+1, 1);
                    int not_buy = getDP(dp, index+1, 0);
                    profit = max(buy, not_buy);
                } else {
                    // sell or dont sell 
                    int sell = +prices[index] + getDP(dp, index+2, 0);
                    int not_sell = getDP(dp, index+1, 1);
                    profit = max(sell, not_sell);
                }

                dp[index][hold] = profit;
            }
        }

        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*2) 
        // Space : O(N*2) for memory 
    }

    int optimise(vector<int>& prices, int N) {
        vector<vector<int>> dp(N, vector<int>(2, 0));

        for (int index = N-1; index >= 0; index--) {
            // buy or dont buy 
            int buy = -prices[index] + getDP(dp, index+1, 1);
            int not_buy = getDP(dp, index+1, 0);
            int b_profit = max(buy, not_buy);

            // sell or dont sell 
            int sell = +prices[index] + getDP(dp, index+2, 0);
            int not_sell = getDP(dp, index+1, 1);
            int s_profit = max(sell, not_sell);

            dp[index][0] = b_profit;
            dp[index][1] = s_profit;
        }

        return dp[0][0];

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N*2) for memory 
    }

public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();

        // recursion 
        // return recursion(prices, N, 0, 0);

        // memoization 
        // vector<vector<int>> dp(N, vector<int>(2, -1));
        // return memoization(prices, N, 0, 0, dp);

        // tabulation 
        // return tabulation(prices, N);

        // optimise 
        return optimise(prices, N);
    }
};

void p2() {
    // Problem 2 : Leetcode 309. Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/buy-stock-with-cooldown/1 

    vector<int> prices = {1,2,3,0,2};

    int profit = Solution2().maxProfit(prices);
    cout << profit << endl;
}


int main() {
    // Day 23 of DP 

    p1();

    p2();


    return 0;
}