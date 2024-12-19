#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(vector<int>& coins, int index, int amount) {
        if (amount == 0) return 1;
        if (index == coins.size()) return 0;

        // we will take coins[index] or skip it 
        int not_pick = recursion(coins, index + 1, amount); // skip 
        int pick = 0;
        if (amount >= coins[index]) pick = recursion(coins, index, amount - coins[index]); // take 

        return (not_pick + pick);

        // Complexity analysis 
        // Time : O(2^N) ~ 
        // Space : O(N) 
    }

    int memoize(vector<int>& coins, int index, int amount, vector<vector<int>>& dp) {
        if (amount == 0) return 1;
        if (index == coins.size()) return 0;

        if (dp[index][amount] != -1) return dp[index][amount];

        // we will take coins[index] or skip it 
        int not_pick = memoize(coins, index + 1, amount, dp);
        int pick = 0;
        if (amount >= coins[index]) pick = memoize(coins, index, amount - coins[index], dp);

        return dp[index][amount] = (not_pick + pick);

        // Complexity analysis 
        // Time : O(2*2*N) ~ 
        // Space : O(N) + O(N*Amount) 
    }

    int tabulation(vector<int>& coins, int N, int tamount) {
        vector<vector<int>> dp(N + 1, vector<int>(tamount + 1, 0));

        // base case 
        for (int index = 0; index <= N; index++) dp[index][0] = 1;

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            for (int amount = 1; amount <= tamount; amount++) {
                // we will take coins[index] or skip it 
                int not_pick = dp[index + 1][amount];
                int pick = 0;
                if (amount >= coins[index]) pick = dp[index][amount - coins[index]];

                dp[index][amount] = (not_pick + pick);
            }
        }

        // return 
        return dp[0][tamount];

        // Complexity analysis 
        // Time : O(N*Amount) 
        // Space : O(N*Amount) 
    }

    int optimised(vector<int>& coins, int N, int tamount) {
        // vector<vector<int>> dp(N+1, vector<int>(tamount+1, 0));
        vector<long long> dpp(tamount + 1, 0);
        dpp[0] = 1;

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            vector<long long> dpn(tamount + 1, 0);
            dpn[0] = 1;

            for (int amount = 1; amount <= tamount; amount++) {
                // we will take coins[index] or skip it 
                int not_pick = dpp[amount];
                int pick = 0;
                if (amount >= coins[index]) pick = dpn[amount - coins[index]];

                dpn[amount] = ((long long)not_pick + pick);
            }

            dpp = dpn;
        }

        // return 
        return dpp[tamount];

        // Complexity analysis 
        // Time : O(N*Amount) 
        // Space : O(2*Amount) 
    }

public:
    int change(int amount, vector<int> coins) {
        int N = coins.size();

        // return recursion(coins, 0, amount);

        // vector<vector<int>> dp(N, vector<int>(amount+1, -1));
        // return memoize(coins, 0, amount, dp);

        // return tabulation(coins, N, amount);

        return optimised(coins, N, amount);
    }
};

void p1() {
    // Problem 1 : Leetcode 518. Coin Change II - https://leetcode.com/problems/coin-change-ii/description/ 

    cout << Problem1().change(5, { 1, 2, 3, 4, 5 }) << endl;
}

class Problem2 {
    int recursion(vector<int>& val, vector<int>& wt, int N, int capacityL, int profit, int index) {
        if (capacityL == 0) return profit;
        if (index == N) return profit;

        int not_pick = recursion(val, wt, N, capacityL, profit, index + 1);
        int pick = 0;
        if (capacityL >= wt[index]) pick = recursion(val, wt, N, capacityL - wt[index], profit + val[index], index);

        return max(not_pick, pick);

        // Complexity analysis 
        // Time : O(2 ^ N) ~ 
        // Space : (N) 
    }

    int memoize(vector<int>& val, vector<int>& wt, int N, int capacityL, int profit, int index, vector<vector<int>>& dp) {
        if (capacityL == 0) return profit;
        if (index == N) return profit;

        if (dp[index][capacityL] != -1) dp[index][capacityL];

        int not_pick = memoize(val, wt, N, capacityL, profit, index + 1, dp);
        int pick = 0;
        if (capacityL >= wt[index]) pick = memoize(val, wt, N, capacityL - wt[index], profit + val[index], index, dp);

        return dp[index][capacityL] = max(not_pick, pick);

        // Complexity analysis 
        // Time : O(2 * 2 * N) ~ 
        // Space : (N) + O(N * Cap) 
    }

    int tabulation(vector<int>& val, vector<int>& wt, int N, int capacity) {
        vector<vector<int>> dp(N + 1, vector<int>(capacity + 1, 0));

        // base case - init with 0 

        for (int index = N - 1; index >= 0; index--) {
            for (int capacityL = 0; capacityL <= capacity; capacityL++) {
                int not_pick = dp[index + 1][capacityL];
                int pick = 0;
                if (capacityL >= wt[index]) pick = dp[index][capacityL - wt[index]] + val[index];

                dp[index][capacityL] = max(not_pick, pick);
            }
        }

        return dp[0][capacity];

        // Complexity analysis 
        // Time : O(N * capacity) 
        // Space : O(N * capacity) 
    }

public:
    int knapSack(vector<int> val, vector<int> wt, int capacity) {
        // code here
        int N = val.size();

        // return recursion(val, wt, val.size(), capacity, 0, 0);

        // vector<vector<int>> dp(N, vector<int>(capacity+1, -1));
        // return memoize(val, wt, N, capacity, 0, 0, dp);

        return tabulation(val, wt, N, capacity);
    }
};

void p2() {
    // Problem 2 : Geeksforgeeks Knapsack with Duplicate Items - https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1 

    cout << Problem2().knapSack({ 1,5,7,2 }, { 1,3,2,1 }, 6) << endl;
}


int main() {
    // Day 19 of December 

    p1();

    p2();


    return 0;
}