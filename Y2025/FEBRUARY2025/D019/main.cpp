#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(vector<int>& prices, int index = 0, bool bought = false, int threshold = 2) {
        if (index == prices.size()) return 0;

        int out = 0;

        if (bought) {
            int sell = +prices[index] + recursion(prices, index + 1, !bought, threshold - 1);
            int hold = recursion(prices, index + 1, bought, threshold);
            out = max(sell, hold);
        }
        else {
            int buy = 0;
            if (threshold > 0) buy = -prices[index] + recursion(prices, index + 1, !bought, threshold);
            int skip = recursion(prices, index + 1, bought, threshold);
            out = max(buy, skip);
        }

        return out;

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) stack space 
    }

    int memoize(vector<int>& prices, vector<vector<vector<int>>>& dp, int index = 0, bool bought = false, int threshold = 2) {
        if (index == prices.size()) return 0;

        if (dp[index][bought][threshold] != -1) return dp[index][bought][threshold];

        int out = 0;

        if (bought) {
            int sell = +prices[index] + memoize(prices, dp, index + 1, !bought, threshold - 1);
            int hold = memoize(prices, dp, index + 1, bought, threshold);
            out = max(sell, hold);
        }
        else {
            int buy = 0;
            if (threshold > 0) buy = -prices[index] + memoize(prices, dp, index + 1, !bought, threshold);
            int skip = memoize(prices, dp, index + 1, bought, threshold);
            out = max(buy, skip);
        }

        return dp[index][bought][threshold] = out;

        // Complexity analysis 
        // Time : O(2*(N*B*T)) 
        // Space : O(N) stack space + O(N*B*T) memory 
    }

    int tabulation(vector<int>& prices, int N, int t = 2) {
        vector<vector<vector<int>>> dp(N + 1, vector<vector<int>>(2, vector<int>(t + 2, 0)));

        // base - handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            for (int bought = 1; bought >= 0; bought--) {
                for (int threshold = t; threshold > 0; threshold--) {
                    int out = 0;

                    if (bought) {
                        int sell = +prices[index] + dp[index + 1][!bought][threshold - 1];
                        int hold = dp[index + 1][bought][threshold];
                        out = max(sell, hold);
                    }
                    else {
                        int buy = -prices[index] + dp[index + 1][!bought][threshold];
                        int skip = dp[index + 1][bought][threshold];
                        out = max(buy, skip);
                    }

                    dp[index][bought][threshold] = out;
                }
            }
        }

        // return 
        return dp[0][0][t];

        // Complexity analysis 
        // Time : O(N*B*T) 
        // Space : O(N*B*T) memory 
    }

    int optimised(vector<int>& prices, int N, int t = 2) {
        vector<vector<int>> next(2, vector<int>(t + 2, 0));

        // base - handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            vector<vector<int>> curr(2, vector<int>(t + 2, 0));

            for (int bought = 1; bought >= 0; bought--) {
                for (int threshold = t; threshold > 0; threshold--) {
                    int out = 0;

                    if (bought) {
                        int sell = +prices[index] + next[!bought][threshold - 1];
                        int hold = next[bought][threshold];
                        out = max(sell, hold);
                    }
                    else {
                        int buy = -prices[index] + next[!bought][threshold];
                        int skip = next[bought][threshold];
                        out = max(buy, skip);
                    }

                    curr[bought][threshold] = out;
                }
            }

            next = curr;
        }

        // return 
        return next[0][t];

        // Complexity analysis 
        // Time : O(N*B*T) 
        // Space : O(B*T) memory 
    }

    int optimised2(vector<int>& prices, int N, int t = 2) {
        vector<vector<int>> next(2, vector<int>(t + 2, 0));

        // base - handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            vector<vector<int>> curr(2, vector<int>(t + 2, 0));
            for (int threshold = t; threshold > 0; threshold--) {
                // bought = 1 
                int sell = +prices[index] + next[!1][threshold - 1];
                int hold = next[1][threshold];
                curr[1][threshold] = max(sell, hold);

                // bought = 0 
                int buy = -prices[index] + next[!0][threshold];
                int skip = next[0][threshold];
                curr[0][threshold] = max(buy, skip);
            }

            next = curr;
        }

        // return 
        return next[0][t];

        // Complexity analysis 
        // Time : O(N*T) 
        // Space : O(B*T) memory 
    }

public:
    int maxProfit(int k, vector<int>& prices) {
        int N = prices.size();
        int threshold = k;

        // return recursion(prices, 0, 0, threshold);

        // vector<vector<vector<int>>> dp(N, vector<vector<int>>(2, vector<int>(threshold+1, -1)));
        // return memoize(prices, dp, 0, 0, threshold);

        // return tabulation(prices, N, threshold);

        // return optimised(prices, N, threshold);

        return optimised2(prices, N, threshold);
    }

    int maxProfit(vector<int>& prices) {
        // return recursion(prices);

        int N = prices.size();
        int threshold = 2;
        // vector<vector<vector<int>>> dp(N, vector<vector<int>>(2, vector<int>(threshold+1, -1)));
        // return memoize(prices, dp);

        // return tabulation(prices, N);

        // return optimised(prices, N);

        return optimised2(prices, N);
    }
};

void p1() {
    // Problem 1 : Leetcode 123. Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1 

    vector<int> prices = { 7,6,4,3,1 };
    cout << Problem1().maxProfit(prices) << endl;
}

void p2() {
    // Problem 2 : Leetcode 188. Best Time to Buy and Sell Stock IV - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-profit4657/1 

    vector<int> prices = { 7,6,7,1,5,1 };
    cout << Problem1().maxProfit(5, prices) << endl;
}

class Problem3 {
    int solve1(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> sqr(m + 1, vector<int>(n + 1, 0));

        int lsqr = 0;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] != '0') {
                    sqr[i][j] = min({ sqr[i][j - 1], sqr[i - 1][j], sqr[i - 1][j - 1] }) + 1;
                }
                lsqr = max(lsqr, sqr[i][j]);
            }
        }

        return (lsqr * lsqr);

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(N*M) 
    }

    int solve2(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> prev(n + 1, 0);

        int lsqr = 0;

        for (int i = 1; i <= m; i++) {
            vector<int> curr(n + 1, 0);

            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] != '0') {
                    curr[j] = min({ curr[j - 1], prev[j], prev[j - 1] }) + 1;
                }
                lsqr = max(lsqr, curr[j]);
            }

            prev = curr;
        }

        return (lsqr * lsqr);

        // Complexity analysis 
        // Time : O(N*M) 
        // Space : O(2*M) 
    }

public:
    int maximalSquare(vector<vector<char>>& matrix) {
        // return solve1(matrix);

        return solve2(matrix);
    }
};

void p3() {
    // Problem 3 : Leetcode 221. Maximal Square -https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix0806/1 

    vector<vector<char>> matrix = {
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
        {'1','1','1','1','1'},
    };
    cout << Problem3().maximalSquare(matrix) << endl;
}


int main() {
    // Day 19 of February 

    p1();

    p2();

    p3();


    return 0;
}