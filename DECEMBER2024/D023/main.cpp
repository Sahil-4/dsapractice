#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(vector<int>& prices, int N, int i, int holding, int t) {
        if (i == N) return 0;

        // if im holding i will hold, if im not holding i will not buy 
        int o1 = recursion(prices, N, i+1, holding, t);
        int o2 = 0;
        if (holding) {
            o2 = +prices[i] + recursion(prices, N, i+1, 0, t-1);
        } else if (!holding && t > 0) {
            o2 = -prices[i] + recursion(prices, N, i+1, 1, t);
        }

        return max(o1, o2);

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) 
    }

    int memoize(vector<int>& prices, int N, int i, int holding, int t, vector<vector<vector<int>>> &dp) {
        if (i == N) return 0;

        if (dp[i][t][holding] != -1) return dp[i][t][holding];

        // if im holding i will hold, if im not holding i will not buy 
        int o1 = memoize(prices, N, i+1, holding, t, dp);
        int o2 = 0;
        if (holding) {
            o2 = +prices[i] + memoize(prices, N, i+1, 0, t-1, dp);
        } else if (!holding && t > 0) {
            o2 = -prices[i] + memoize(prices, N, i+1, 1, t, dp);
        }

        return dp[i][t][holding] = max(o1, o2);

        // Complexity analysis 
        // Time : O(2 * N*t*holding) 
        // Space : O(N) + O(N*t*holding) 
    }

    int tabulation(vector<int>& prices, int N, int tt) {
        vector<vector<vector<int>>> dp(N+1, vector<vector<int>>(tt+1, vector<int>(2, 0)));

        // base - handled 

        // recurrence 
        for (int i = N-1; i >= 0; i--) {
            for (int t = 1; t <= tt; t++) {
                for (int holding = 0; holding <= 1; holding++) {
                    int o1 = dp[i+1][t][holding];
                    int o2 = 0;
                    if (holding) {
                        o2 = +prices[i] + dp[i+1][t-1][0];
                    } else if (!holding && t > 0) {
                        o2 = -prices[i] + dp[i+1][t][1];
                    }
                    dp[i][t][holding] = max(o1, o2);
                } 
            }
        }

        // return 
        return dp[0][tt][0];

        // Complexity analysis 
        // Time : O(N*t*holding) 
        // Space : O(N*t*holding) 
    }

    int optimised(vector<int>& prices, int N, int tt) {
        vector<vector<int>> dpp(tt+1, vector<int>(2, 0));

        // base - handled 

        // recurrence 
        for (int i = N-1; i >= 0; i--) {
            vector<vector<int>> dpc(tt+1, vector<int>(2, 0));

            for (int t = 1; t <= tt; t++) {
                {
                    // int holding = 0;
                    int o1 = dpp[t][0];
                    int o2 = 0;
                    if (t > 0) o2 = -prices[i] + dpp[t][1];
                    dpc[t][0] = max(o1, o2);
                }
                {
                    // int holding = 1;
                    int o1 = dpp[t][1];
                    int o2 = +prices[i] + dpp[t-1][0];
                    dpc[t][1] = max(o1, o2);
                }
            }

            dpp = dpc;
        }

        // return 
        return dpp[tt][0];

        // Complexity analysis 
        // Time : O(N*t) 
        // Space : O(2*t*holding) 
    }

public:
    int maxProfit(vector<int> prices) {
        int N = prices.size();
        int t = 2;

        // return recursion(prices, N, 0, 0, t);

        // index -> t -> holding 
        // vector<vector<vector<int>>> dp(N, vector<vector<int>>(t+1, vector<int>(2, -1)));
        // return memoize(prices, N, 0, 0, t, dp);

        // return tabulation(prices, N, t);

        return optimised(prices, N, t);
    }
};

void p1() {
    // Problem 1 : Leetcode 123. Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/ 

    cout << Problem1().maxProfit({ 1,2,3,4,5 }) << endl;
    cout << Problem1().maxProfit({ 5,4,3,2,1 }) << endl;
    cout << Problem1().maxProfit({ 1,1,5,4,3,6,8 }) << endl;
}

class Problem2 {
    long long recursion(vector<long long>& prices, int N, int i, int holding) {
        if (i >= N) return 0;

        // if im holding i will hold, if im not holding i will not buy 
        long long o1 = recursion(prices, N, i+1, holding);
        long long o2 = 0;
        if (holding) {
            o2 = +prices[i] + recursion(prices, N, i+2, 0);
        } else {
            o2 = -prices[i] + recursion(prices, N, i+1, 1);
        }

        return max(o1, o2);

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) 
    }

    long long memoize(vector<long long>& prices, int N, int i, int holding, vector<vector<long long>> &dp) {
        if (i >= N) return 0;

        if (dp[i][holding] != -1) return dp[i][holding];

        // if im holding i will hold, if im not holding i will not buy 
        long long o1 = memoize(prices, N, i+1, holding, dp);
        long long o2 = 0;
        if (holding) {
            o2 = +prices[i] + memoize(prices, N, i+2, 0, dp);
        } else {
            o2 = -prices[i] + memoize(prices, N, i+1, 1, dp);
        }

        return dp[i][holding] = max(o1, o2);

        // Complexity analysis 
        // Time : O(2 * N*holding) 
        // Space : O(N) + O(N*holding) 
    }

    long long tabulation(vector<long long>& prices, int N) {
        vector<vector<long long>> dp(N+2, vector<long long>(2, 0));

        // base - handled 

        // recurrence 
        for (int i = N-1; i >= 0; i--) {
            for (int holding = 0; holding <= 1; holding++) {
                long long o1 = dp[i+1][holding];
                long long o2 = 0;
                if (holding) {
                    o2 = +prices[i] + dp[i+2][0];
                } else {
                    o2 = -prices[i] + dp[i+1][1];
                }
                dp[i][holding] = max(o1, o2);
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*t*holding) 
        // Space : O(N*t*holding) 
    }

public:
    long long maximumProfit(vector<long long> prices, int N) {
        // Code here 

        // return recursion(prices, N, 0, 0);

        // vector<vector<long long>> dp(N, vector<long long>(2, -1));
        // return memoize(prices, N, 0, 0, dp);

        return tabulation(prices, N);
    }
};

void p2() {
    // Problem 2 : Geeksforgeeks Stock Buy and Sell – with Cooldown - https://www.geeksforgeeks.org/problems/buy-stock-with-cooldown/1 

    cout << Problem2().maximumProfit({ 1,2,3,4,5 }, 5) << endl;
    cout << Problem2().maximumProfit({ 5,4,3,2,1 }, 5) << endl;
    cout << Problem2().maximumProfit({ 1,1,5,4,3,6,8 }, 7) << endl;
}


int main() {
    // Day 23 of December 

    p1();

    p2();


    return 0;
}