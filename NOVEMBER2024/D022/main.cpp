#include <iostream>
#include <vector>

using namespace std;

class Problem1 {
public:
    int maxProfit(vector<int>& prices) {
        int N = prices.size();

        // memory 
        int profit = 0;
        int buyDay = 0;

        for (int sellDay = buyDay + 1; sellDay < N; sellDay++) {
            // perform operations using data in memory 
            int tp = prices[sellDay] - prices[buyDay];
            profit = max(profit, tp);

            // update memory 
            if (prices[buyDay] > prices[sellDay]) buyDay = sellDay;
        }

        return profit;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }
};

void p1() {
    // Problem 1 : Leetcode 121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/buy-stock-2/1 

    vector<int> prices = { 7,1,5,3,6,4 };
    int profit = Problem1().maxProfit(prices);
    cout << profit << endl;
}

class Problem2 {
public:
    int recursion(vector<int>& prices, int N, int index, int canBuy) {
        if (index == N) return 0;

        int profit = 0;

        if (canBuy) {
            int buy = -prices[index] + recursion(prices, N, index + 1, 0);
            int not_buy = recursion(prices, N, index + 1, 1);
            profit = max(buy, not_buy);
        } else {
            int sell = +prices[index] + recursion(prices, N, index + 1, 1);
            int not_sell = recursion(prices, N, index + 1, 0);
            profit = max(sell, not_sell);
        }

        return profit;

        // Complexity analysis 
        // Time : O(2^(2N)) 
        // Space : O(2N) stack space 
    }

    int memoization(vector<int>& prices, int N, int index, int canBuy, vector<vector<int>>& dp) {
        if (index == N) return 0;

        if (dp[index][canBuy] != -1) return dp[index][canBuy];

        int profit = 0;

        if (canBuy) {
            int buy = -prices[index] + memoization(prices, N, index + 1, 0, dp);
            int not_buy = memoization(prices, N, index + 1, 1, dp);
            profit = max(buy, not_buy);
        } else {
            int sell = +prices[index] + memoization(prices, N, index + 1, 1, dp);
            int not_sell = memoization(prices, N, index + 1, 0, dp);
            profit = max(sell, not_sell);
        }

        return dp[index][canBuy] = profit;

        // Complexity analysis 
        // Time : O(2*(2N)) 
        // Space : O(2N) stack space + O(2N) for memoization 
    }

    int tabulation(vector<int>& prices, int N) {
        vector<vector<int>> dp(N + 1, vector<int>(2, 0));

        for (int index = N - 1; index >= 0; index--) {
            for (int canBuy = 0; canBuy < 2; canBuy++) {
                int profit = 0;

                if (canBuy) {
                    int buy = -prices[index] + dp[index + 1][0];
                    int not_buy = dp[index + 1][1];
                    profit = max(buy, not_buy);
                } else {
                    int sell = +prices[index] + dp[index + 1][1];
                    int not_sell = dp[index + 1][0];
                    profit = max(sell, not_sell);
                }

                dp[index][canBuy] = profit;
            }
        }

        return dp[0][1];

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(2N) for memory 
    }

    int optimised(vector<int>& prices, int N) {
        // vector<vector<int>> dp(N+1, vector<int>(2, 0));
        vector<int> dpn(2, 0);

        for (int index = N - 1; index >= 0; index--) {
            int buy = -prices[index] + dpn[0];
            int not_buy = dpn[1];
            int buy_profit = max(buy, not_buy);

            int sell = +prices[index] + dpn[1];
            int not_sell = dpn[0];
            int sell_profit = max(sell, not_sell);

            dpn[0] = sell_profit;
            dpn[1] = buy_profit;
        }

        return dpn[1];

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(2) for memory 
    }

    int maxProfit(vector<int>& prices) {
        int N = prices.size();

        // recursion 
        // return recursion(prices, N, 0, true);

        // memoization 
        // vector<vector<int>> dp(N, vector<int>(2, -1));
        // return memoization(prices, N, 0, 1, dp);

        // tabulation 
        // return tabulation(prices, N);

        // optimised 
        return optimised(prices, N);
    }
};

void p2() {
    // Problem 2 : Leetcode 122. Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1  

    vector<int> prices = { 7,1,5,3,6,4 };
    int profit = Problem2().maxProfit(prices);
    cout << profit << endl;
}

class Problem3 {
public:
    int recursion(vector<int>& prices, int N, int index, int canBuy, int cap) {
        if (cap == 0) return 0;
        if (index == N) return 0;

        int profit = 0;

        if (canBuy) {
            int buy = 0;
            if (cap > 0) buy = -prices[index] + recursion(prices, N, index + 1, 0, cap);
            int not_buy = recursion(prices, N, index + 1, 1, cap);
            profit = max(buy, not_buy);
        } else {
            int sell = +prices[index] + recursion(prices, N, index + 1, 1, cap - 1);
            int not_sell = recursion(prices, N, index + 1, 0, cap);
            profit = max(sell, not_sell);
        }

        return profit;

        // Complexity analysis 
        // Time : O(2^(2*N)) 
        // Space : O(2*2*N) for stack space 
    }

    int memoization(vector<int>& prices, int N, int index, int canBuy, int cap, vector<vector<vector<int>>>& dp) {
        if (cap == 0) return 0;
        if (index == N) return 0;

        if (dp[index][canBuy][cap] != -1) return dp[index][canBuy][cap];

        int profit = 0;

        if (canBuy) {
            int buy = 0;
            if (cap > 0) buy = -prices[index] + memoization(prices, N, index + 1, 0, cap, dp);
            int not_buy = memoization(prices, N, index + 1, 1, cap, dp);
            profit = max(buy, not_buy);
        } else {
            int sell = +prices[index] + memoization(prices, N, index + 1, 1, cap - 1, dp);
            int not_sell = memoization(prices, N, index + 1, 0, cap, dp);
            profit = max(sell, not_sell);
        }

        return dp[index][canBuy][cap] = profit;

        // Complexity analysis 
        // Time : O(2*2*2*N) 
        // Space : O(2*2*N) for stack space + O(N*2*2) for memory 
    }

    int tabulation(vector<int>& prices, int N, int capK) {
        vector<vector<vector<int>>> dp(N + 1, vector<vector<int>>(2, vector<int>(capK + 1, 0)));

        // base case - already handled 

        for (int index = N - 1; index >= 0; index--) {
            for (int cap = capK; cap > 0; cap--) {
                for (int canBuy = 1; canBuy >= 0; canBuy--) {
                    int profit = 0;

                    if (canBuy) {
                        int buy = -prices[index] + dp[index + 1][0][cap];
                        int not_buy = dp[index + 1][1][cap];
                        profit = max(buy, not_buy);
                    } else {
                        int sell = +prices[index] + dp[index + 1][1][cap - 1];
                        int not_sell = dp[index + 1][0][cap];
                        profit = max(sell, not_sell);
                    }

                    dp[index][canBuy][cap] = profit;
                }
            }
        }

        return dp[0][1][capK];

        // Complexity analysis 
        // Time : O(N*2*2) 
        // Space : O((N+1)*2*2) for memory 
    }

    int optimised(vector<int>& prices, int N, int capK) {
        vector<vector<int>> dpn(2, vector<int>(capK + 1, 0));

        // base case - already handled 

        for (int index = N - 1; index >= 0; index--) {
            vector<vector<int>> dpc(2, vector<int>(capK + 1, 0));

            for (int cap = capK; cap > 0; cap--) {
                for (int canBuy = 1; canBuy >= 0; canBuy--) {
                    int profit = 0;

                    if (canBuy) {
                        int buy = -prices[index] + dpn[0][cap];
                        int not_buy = dpn[1][cap];
                        profit = max(buy, not_buy);
                    } else {
                        int sell = +prices[index] + dpn[1][cap - 1];
                        int not_sell = dpn[0][cap];
                        profit = max(sell, not_sell);
                    }

                    dpc[canBuy][cap] = profit;
                }
            }

            dpn = dpc;
        }

        return dpn[1][capK];

        // Complexity analysis 
        // Time : O(N*2*2) 
        // Space : O(2*2) for memory 
    }

    int maxProfit(vector<int>& prices) {
        int N = prices.size();
        int cap = 2;

        // recursion 
        // return recursion(prices, N, 0, true, 2);

        // memoization 
        // vector<vector<vector<int>>> dp(N, vector<vector<int>>(2, vector<int>(cap+1, -1)));
        // return memoization(prices, N, 0, 1, cap, dp);

        // tabulation 
        // return tabulation(prices, N, cap);

        // optimised 
        return optimised(prices, N, cap);
    }
};

void p3() {
    // Problem 3 : Leetcode 123. Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1 

    vector<int> prices = { 3,3,5,0,0,3,1,4 };
    int profit = Problem3().maxProfit(prices);
    cout << profit << endl;
}


int main() {
    // Day 22 of DP 

    p1();

    p2();

    p3();


    return 0;
}