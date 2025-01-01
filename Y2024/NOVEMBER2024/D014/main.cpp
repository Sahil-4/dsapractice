#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int MODO = (int)1e9 + 7;

int recursionP1(int arr[], int index, int sum) {
    if (index == 0) {
        int count = 0;
        if (sum == 0) count++;
        if (sum - arr[index] == 0) count++;
        return count;
    }

    int not_pick = recursionP1(arr, index - 1, sum);
    int pick = 0;
    if (arr[index] <= sum) pick = recursionP1(arr, index - 1, sum - arr[index]);

    return (not_pick + pick);

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) for stack space 
}

int memoizeP1(int arr[], int index, int sum, vector<vector<int>>& dp) {
    if (index == 0) {
        int count = 0;
        if (sum == 0) count++;
        if (sum - arr[index] == 0) count++;
        return count;
    }

    if (dp[index][sum] != -1) return dp[index][sum];

    int not_pick = memoizeP1(arr, index - 1, sum, dp);
    int pick = 0;
    if (arr[index] <= sum) pick = memoizeP1(arr, index - 1, sum - arr[index], dp);

    int out = (((not_pick % MODO) + (pick % MODO)) % MODO);
    return dp[index][sum] = out;

    // Complexity analysis 
    // Time : O(2*N) 
    // Space : O(N) for stack space + O(N * SUM) for memoization 
}

int tabulationP1(int arr[], int N, int SUM) {
    vector<vector<int>> dp(N, vector<int>(SUM + 1, 0));

    for (int i = 0; i < N; i++) dp[i][0] = 1;
    if (arr[0] <= SUM && arr[0] != 0) dp[0][arr[0]] = 1;
    if (arr[0] == 0) dp[0][0] = 2;

    for (int i = 1; i < N; i++) {
        for (int s = 0; s <= SUM; s++) {
            int not_pick = dp[i - 1][s] % MODO;
            int pick = 0;
            if (arr[i] <= s) pick = dp[i - 1][s - arr[i]] % MODO;

            dp[i][s] = (not_pick + pick) % MODO;
        }
    }

    return dp[N - 1][SUM];

    // Complexity analysis 
    // Time : O(N*SUM) 
    // Space : O(N * SUM) for memoization 
}

int optimiseP1(int arr[], int N, int SUM) {
    vector<int> dp(SUM + 1, 0);
    vector<int> dpc(SUM + 1);

    dp[0] = dpc[0] = 1;
    if (arr[0] <= SUM && arr[0] != 0) dp[arr[0]] = 1;
    if (arr[0] == 0) dp[0] = 2;

    for (int i = 1; i < N; i++) {
        for (int s = 0; s <= SUM; s++) {
            int not_pick = dp[s] % MODO;
            int pick = 0;
            if (arr[i] <= s) pick = dp[s - arr[i]] % MODO;

            dpc[s] = (pick + not_pick) % MODO;
        }

        dp = dpc;
    }

    return dp[SUM];

    // Complexity analysis 
    // Time : O(N*SUM) 
    // Space : O(SUM) for memoization 
}

int perfectSum(int arr[], int n, int sum) {
    // Your code goes here

    // recursion 
    // return recursionP1(arr, n - 1, sum);

    // memoize 
    // vector<vector<int>> dp(n, vector<int>(sum+1, -1));
    // return memoizeP1(arr, n - 1, sum, dp);

    // tabulation 
    // return tabulationP1(arr, n, sum);

    // space optimises 
    return optimiseP1(arr, n, sum);
}

void p1() {
    // Problem 1 : Geeksforgeeks Perfect Sum Problem Geeksforgeeks - https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1 

    int n = 9;
    int arr[] = { 0,0,0,0,0,0,0,0,1 };
    int t = 1;

    int sum = perfectSum(arr, n, t);
    cout << sum << endl;
}

int countPartitions(int n, int d, int arr[]) {
    // Code here
    int tsum = accumulate(arr, arr + n, 0);

    if (((tsum - d) < 0) || ((tsum - d) & 1)) return 0;

    return perfectSum(arr, n, (tsum - d) / 2);
}

void p2() {
    // Problem 2 : Geeksforgeeks Partitions with Given Difference - https://www.geeksforgeeks.org/problems/partitions-with-given-difference/0 

    int n = 4;
    int d = 3;
    int arr[] = { 5, 2, 6, 4 };

    int ps = countPartitions(n, d, arr);
    cout << ps << endl;
}

int BOUND = (int)1e9;

int recursionP3(vector<int>& coins, int i, int t) {
    if (t == 0) return 0;
    if (i == 0) {
        if (t % coins[i] == 0) return t / coins[i];
        return BOUND;
    }

    int not_take = recursionP3(coins, i - 1, t);
    int take = BOUND;
    if (coins[i] <= t) take = 1 + recursionP3(coins, i, t - coins[i]);

    return min(not_take, take);

    // Complexity analysis 
    // Time : O(2^t) ~
    // Space : O(t) ~ for recursion stack space 
}

int memoizeP3(vector<int>& coins, int i, int t, vector<vector<int>>& dp) {
    if (t == 0) return 0;
    if (i == 0) {
        if (t % coins[i] == 0) return t / coins[i];
        return BOUND;
    }

    if (dp[i][t] != -1) return dp[i][t];

    int not_take = memoizeP3(coins, i - 1, t, dp);
    int take = BOUND;
    if (coins[i] <= t) take = 1 + memoizeP3(coins, i, t - coins[i], dp);

    return dp[i][t] = min(not_take, take);

    // Complexity analysis 
    // Time : O(n*t) ~
    // Space : O(t) ~ for recursion stack space + O(N * t) for memoization 
}

int tabulationP3(vector<int>& coins, int N, int amt) {
    vector<vector<int>> dp(N, vector<int>(amt + 1, 0));

    // base case 
    for (int t = 0; t <= amt; t++) {
        if (t % coins[0] == 0) {
            dp[0][t] = t / coins[0];
        }
        else {
            dp[0][t] = BOUND;
        }
    }

    for (int i = 1; i < N; i++) {
        for (int t = 0; t <= amt; t++) {
            int not_take = dp[i - 1][t];
            int take = BOUND;
            if (coins[i] <= t) take = 1 + dp[i][t - coins[i]];

            dp[i][t] = min(not_take, take);
        }
    }

    return dp[N - 1][amt];

    // Complexity analysis 
    // Time : O(N*amt) 
    // Space : O(N*amt) 
}

int optimiseP3(vector<int>& coins, int N, int amt) {
    vector<int> dp(amt + 1, 0);

    // base case 
    for (int t = 0; t <= amt; t++) {
        if (t % coins[0] == 0) {
            dp[t] = t / coins[0];
        }
        else {
            dp[t] = BOUND;
        }
    }

    for (int i = 1; i < N; i++) {
        vector<int> dpc(amt + 1, 0);

        for (int t = 0; t <= amt; t++) {
            int not_take = dp[t];
            int take = BOUND;
            if (coins[i] <= t) take = 1 + dpc[t - coins[i]];

            dpc[t] = min(not_take, take);
        }

        dp = dpc;
    }

    return dp[amt];

    // Complexity analysis 
    // Time : O(N*amt) 
    // Space : O(N*amt) 
}

int coinChange(vector<int>& coins, int amount) {
    int N = coins.size();

    // recursion 
    // int out = recursionP3(coins, N - 1, amount);
    // return out != (int) 1e9 ? out : -1;

    // memoize 
    // vector<vector<int>> dp(N, vector<int>(amount + 1, -1));
    // int out = memoizeP3(coins, N - 1, amount, dp);
    // return out != BOUND ? out : -1;

    // tabulation 
    // int out = tabulationP3(coins, N, amount);
    // return out != BOUND ? out : -1;

    // space optimise 
    int out = optimiseP3(coins, N, amount);
    return out != BOUND ? out : -1;
}

void p3() {
    // Problem 3 : Leetcode 322. Coin Change - https://leetcode.com/problems/coin-change/description/ 

    vector<int> coins = { 12,4,16,19 };
    int amount = 152;

    int ns = coinChange(coins, amount);
    cout << ns << endl;
}

int main() {
    // Day 14 of DP 

    p1();

    p2();

    p3();


    return 0;
}