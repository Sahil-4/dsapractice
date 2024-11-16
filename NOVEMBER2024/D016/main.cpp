#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int recursion(vector<int>& coins, int index, int amount) {
    // base case 
    if (index == 0) {
        if (amount % coins[index] == 0) return 1;
        return 0;
    }

    // recurrence 
    int not_pick = recursion(coins, index - 1, amount);
    int pick = 0;
    if (amount >= coins[index]) pick = recursion(coins, index, amount - coins[index]);

    // return - conclude 
    return (not_pick + pick);

    // Complexity analysis 
    // Time : O(2^N) ~ 
    // Space : O(N) ~ recursion stack space 
}

int memoize(vector<int>& coins, int index, int amount, vector<vector<int>>& dp) {
    // base case 
    if (index == 0) {
        if (amount % coins[index] == 0) return 1;
        return 0;
    }

    if (dp[index][amount] != -1) return dp[index][amount];

    // recurrence 
    int not_pick = memoize(coins, index - 1, amount, dp);
    int pick = 0;
    if (amount >= coins[index]) pick = memoize(coins, index, amount - coins[index], dp);

    // return - conclude 
    return dp[index][amount] = (not_pick + pick);

    // Complexity analysis 
    // Time : O(N) ~ 
    // Space : O(N) ~ recursion stack space + O(N * amount) for memoization 
}

int tabulation(vector<int>& coins, int N, int amount) {
    vector<vector<int>> dp(N, vector<int>(amount + 1, 0));

    // base case 
    for (int amt = 0; amt <= amount; amt++) {
        if (amt % coins[0] == 0) {
            dp[0][amt] = 1;
        }
    }

    for (int index = 1; index < N; index++) {
        for (int amt = 0; amt <= amount; amt++) {
            int not_pick = dp[index - 1][amt];
            int pick = 0;
            if (amt >= coins[index]) pick = dp[index][amt - coins[index]];

            dp[index][amt] = (not_pick + pick);
        }
    }

    return dp[N - 1][amount];
    // Complexity analysis 
    // Time : O(N * amount) 
    // Space : O(N * amount) for memoization 
}

int optimise(vector<int>& coins, int N, int amount) {
    vector<long long> dpp(amount + 1, 0);

    // base case 
    for (int amt = 0; amt <= amount; amt++) {
        if (amt % coins[0] == 0) {
            dpp[amt] = 1;
        }
    }

    for (int index = 1; index < N; index++) {
        vector<long long> dpc(amount + 1, 0);

        for (int amt = 0; amt <= amount; amt++) {
            int not_pick = dpp[amt];
            int pick = 0;
            if (amt >= coins[index]) pick = dpc[amt - coins[index]];

            dpc[amt] = ((long long)not_pick + pick);
        }

        dpp = dpc;
    }

    return dpp[amount];
    // Complexity analysis 
    // Time : O(N * amount) 
    // Space : O(amount) for memoization 
}

int change(int amount, vector<int>& coins) {
    int N = coins.size();

    // recursion - try all possibile combinations and chack for validity 
    // return recursion(coins, N - 1, amount);

    // memoize 
    // vector<vector<int>> dp(N, vector<int>(amount + 1, -1));
    // return memoize(coins, N - 1, amount, dp);

    // tabulation 
    // return tabulation(coins, N, amount);

    // space optimise 
    return optimise(coins, N, amount);
}

void p1() {
    // Problem 1 : Leetcode 518. Coin Change II - https://leetcode.com/problems/coin-change-ii/description/ 

    int amount = 1000;
    vector<int> coins = { 3,5,7,8,9,10,11 };

    int ways = change(amount, coins);
    cout << ways << endl;
}

int __recursion(vector<int>& value, vector<int>& weight, int capacity, int index) {
    if (index == 0) {
        if (capacity >= weight[index]) {
            return ((capacity / weight[index]) * value[index]);
        }
        return 0;
    }

    int not_pick = __recursion(value, weight, capacity, index - 1);
    int pick = 0;
    if (capacity >= weight[index]) {
        pick = value[index] + __recursion(value, weight, capacity - weight[index], index);
    }

    return max(not_pick, pick);

    // Complexity analysis 
    // Time : O(2^N) ~ 
    // Space : O(N) ~ 
}

int __memoization(vector<int>& value, vector<int>& weight, int capacity, int index, vector<vector<int>>& dp) {
    if (index == 0) {
        if (capacity >= weight[index]) {
            return ((capacity / weight[index]) * value[index]);
        }
        return 0;
    }

    if (dp[index][capacity] != -1) return dp[index][capacity];

    int not_pick = __memoization(value, weight, capacity, index - 1, dp);
    int pick = 0;
    if (capacity >= weight[index]) {
        pick = value[index] + __memoization(value, weight, capacity - weight[index], index, dp);
    }

    return dp[index][capacity] = max(not_pick, pick);

    // Complexity analysis 
    // Time : O(2*N) ~ 
    // Space : O(N) ~ + O(N * capacity) for memoization 
}

int __tabulation(vector<int>& value, vector<int>& weight, int capacity, int N) {
    vector<vector<int>> dp(N, vector<int>(capacity + 1, 0));

    // base case 
    for (int cap = 0; cap <= capacity; cap++) {
        if (cap >= weight[0]) {
            dp[0][cap] = ((cap / weight[0]) * value[0]);
        }
    }

    for (int index = 1; index < N; index++) {
        for (int cap = 0; cap <= capacity; cap++) {
            int not_pick = dp[index - 1][cap];
            int pick = 0;
            if (cap >= weight[index]) {
                pick = value[index] + dp[index][cap - weight[index]];
            }

            dp[index][cap] = max(not_pick, pick);
        }
    }

    // return 
    return dp[N - 1][capacity];

    // Complexity analysis 
    // Time : O(N * capacity) 
    // Space : O(N * capacity) for memoization 
}

int __optimise(vector<int>& value, vector<int>& weight, int capacity, int N) {
    vector<int> dpp(capacity + 1, 0);

    // base case 
    for (int cap = 0; cap <= capacity; cap++) {
        if (cap >= weight[0]) {
            dpp[cap] = ((cap / weight[0]) * value[0]);
        }
    }

    for (int index = 1; index < N; index++) {
        vector<int> dpc(capacity + 1, 0);
        for (int cap = 0; cap <= capacity; cap++) {
            int not_pick = dpp[cap];
            int pick = 0;
            if (cap >= weight[index]) {
                pick = value[index] + dpc[cap - weight[index]];
            }

            dpc[cap] = max(not_pick, pick);
        }

        dpp = dpc;
    }

    // return 
    return dpp[capacity];

    // Complexity analysis 
    // Time : O(N * capacity) 
    // Space : O(N * capacity) for memoization 
}

int knapSack(int capacity, vector<int>& val, vector<int>& wt) {
    // code here
    int N = val.size();

    // recursion 
    // return __recursion(val, wt, capacity, N - 1);

    // memoization 
    // vector<vector<int>> dp(N, vector<int>(capacity + 1, -1));
    // return __memoization(val, wt, capacity, N - 1, dp);

    // tabulation 
    // return __tabulation(val, wt, capacity, N);

    // space optimise 
    return __optimise(val, wt, capacity, N);
}

void p2() {
    // Problem 2 : Geeksforgeeks Knapsack with Duplicate Items - https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1 

    int capacity = 8;
    vector<int> val = { 6, 1, 7, 7 };
    vector<int> wt = { 1, 3, 4, 5 };

    int profit = knapSack(capacity, val, wt);
    cout << profit << endl;
}

int ___recursion(int prices[], int index, int N) {
    if (index == 0) {
        return N * prices[index];
    }

    int not_take = ___recursion(prices, index - 1, N);
    int take = INT_MIN;
    int rlen = index + 1;
    if (rlen <= N) {
        take = prices[index] + ___recursion(prices, index, N - rlen);
    }

    return max(not_take, take);

    // Complexity analysis 
    // Time : O(2^N) ~ 
    // Space : O(N) ~ recursion stack space 
}

int ___memoization(int prices[], int index, int N, vector<vector<int>>& dp) {
    if (index == 0) {
        return N * prices[index];
    }

    if (dp[index][N] != -1) return dp[index][N];

    int not_take = ___memoization(prices, index - 1, N, dp);
    int take = INT_MIN;
    int rlen = index + 1;
    if (rlen <= N) {
        take = prices[index] + ___memoization(prices, index, N - rlen, dp);
    }

    return dp[index][N] = max(not_take, take);

    // Complexity analysis 
    // Time : O(2*N) ~ 
    // Space : O(N) ~ recursion stack space + O(N * N) for memoization 
}

int ___tabulation(int prices[], int N) {
    vector<vector<int>> dp(N, vector<int>(N + 1, 0));

    // base case 
    for (int rlen = 0; rlen <= N; rlen++) {
        dp[0][rlen] = prices[0] * rlen;
    }

    // recursion copy 
    for (int index = 1; index < N; index++) {
        for (int rlen = 0; rlen <= N; rlen++) {
            int not_take = dp[index - 1][rlen];
            int take = INT_MIN;
            int rod = index + 1;
            if (rod <= rlen) take = prices[index] + dp[index][rlen - rod];

            dp[index][rlen] = max(not_take, take);
        }
    }

    // return 
    return dp[N - 1][N];

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(N * N) for memoization 
}

int ___optimise(int prices[], int N) {
    vector<int> dpp(N + 1, 0);

    // base case 
    for (int rlen = 0; rlen <= N; rlen++) {
        dpp[rlen] = prices[0] * rlen;
    }

    // recursion copy 
    for (int index = 1; index < N; index++) {
        vector<int> dpc(N + 1, 0);

        for (int rlen = 0; rlen <= N; rlen++) {
            int not_take = dpp[rlen];
            int take = INT_MIN;
            int rod = index + 1;
            if (rod <= rlen) take = prices[index] + dpc[rlen - rod];

            dpc[rlen] = max(not_take, take);
        }

        dpp = dpc;
    }

    // return 
    return dpp[N];

    // Complexity analysis 
    // Time : O(N * N) 
    // Space : O(N * N) for memoization 
}

int cutRod(int prices[], int N) {
    // code here 

    // recursion 
    // return ___recursion(prices, N - 1, N);

    // memoization 
    // vector<vector<int>> dp(N, vector<int>(N + 1, -1));
    // return ___memoization(prices, N - 1, N, dp);

    // tabulation 
    // return ___tabulation(prices, N);

    // space optimise 
    return ___optimise(prices, N);
}

void p3() {
    // Problem 3 : Geeksforgeeks Rod Cutting - https://www.geeksforgeeks.org/problems/rod-cutting0840/1 

    int prices[] = { 1, 5, 8, 9, 10, 17, 17, 20 };
    int N = 8;

    int profit = cutRod(prices, N);
    cout << profit << endl;
}


int main() {
    // Day 16 of DP 

    p1();

    p2();

    p3();


    return 0;
}