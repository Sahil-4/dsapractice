#include <iostream>
#include <vector>

using namespace std;


int recursion(vector<int>& prices, int& N, int index, int& fee, int holding) {
    if (index == N) return 0;

    int profit = 0;

    if (!holding) {
        int buy = -prices[index] + recursion(prices, N, index + 1, fee, 1);
        int not_buy = recursion(prices, N, index + 1, fee, 0);
        profit = max(buy, not_buy);
    } else {
        int sell = -fee + prices[index] + recursion(prices, N, index + 1, fee, 0);
        int not_sell = recursion(prices, N, index + 1, fee, 1);
        profit = max(sell, not_sell);
    }

    return profit;

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) for recursion call stack 
}

int memoization(vector<int>& prices, int& N, int index, int& fee, int holding, vector<vector<int>>& dp) {
    if (index == N) return 0;

    if (dp[index][holding] != -1) return dp[index][holding];

    int profit = 0;

    if (!holding) {
        int buy = -prices[index] + memoization(prices, N, index + 1, fee, 1, dp);
        int not_buy = memoization(prices, N, index + 1, fee, 0, dp);
        profit = max(buy, not_buy);
    } else {
        int sell = -fee + prices[index] + memoization(prices, N, index + 1, fee, 0, dp);
        int not_sell = memoization(prices, N, index + 1, fee, 1, dp);
        profit = max(sell, not_sell);
    }

    return dp[index][holding] = profit;

    // Complexity analysis 
    // Time : O(2*2*N) 
    // Space : O(N) for recursion call stack + O(2N) for memory 
}

int tabulation(vector<int>& prices, int& N, int fee) {
    vector<vector<int>> dp(N + 1, vector<int>(2, 0));

    // base - already heandled in init 

    // recurrence 
    for (int index = N - 1; index >= 0; index--) {
        for (int holding = 1; holding >= 0; holding--) {
            int profit = 0;

            if (!holding) {
                int buy = -prices[index] + dp[index + 1][1];
                int not_buy = dp[index + 1][0];
                profit = max(buy, not_buy);
            } else {
                int sell = -fee + prices[index] + dp[index + 1][0];
                int not_sell = dp[index + 1][1];
                profit = max(sell, not_sell);
            }

            dp[index][holding] = profit;
        }
    }

    // return 
    return dp[0][0];

    // Complexity analysis 
    // Time : O(N*2) 
    // Space : O(2N) for memory 
}

int optimise(vector<int>& prices, int& N, int fee) {
    vector<int> dpn(2, 0);

    // base - already heandled in init 

    // recurrence 
    for (int index = N - 1; index >= 0; index--) {
        vector<int> dpc(2, 0);

        int buy = -prices[index] + dpn[1];
        int not_buy = dpn[0];
        int b_profit = max(buy, not_buy);

        int sell = -fee + prices[index] + dpn[0];
        int not_sell = dpn[1];
        int s_profit = max(sell, not_sell);

        dpc[0] = b_profit;
        dpc[1] = s_profit;

        dpn = dpc;
    }

    // return 
    return dpn[0];

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(2) for memory 
}

int maxProfit(vector<int>& prices, int fee) {
    int N = prices.size();

    // recursion 
    // return recursion(prices, N, 0, fee, 0);

    // memoization 
    // vector<vector<int>> dp(N, vector<int>(2, -1));
    // return memoization(prices, N, 0, fee, 0, dp);

    // tabulation 
    // return tabulation(prices, N, fee);

    // optimised 
    return optimise(prices, N, fee);
}

void p1() {
    // Problem 1 : Leetcode 714. Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/buy-stock-with-transaction-fee/1 

    vector<int> prices = { 1, 3, 2, 8, 4, 9 };
    int fee = 2;

    int profit = maxProfit(prices, fee);
    cout << profit << endl;
}


int main() {
    // Day 24 of DP 

    p1();


    return 0;
}