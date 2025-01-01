#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int recursion(vector<int>& values, vector<int>& weights, int index, int capacityLeft) {
    if (capacityLeft == 0) return 0;
    if (index == 0) {
        if (capacityLeft >= weights[index]) return values[index];
        return 0;
    }

    int not_pick = recursion(values, weights, index - 1, capacityLeft);
    int pick = 0;
    if (capacityLeft >= weights[index]) {
        pick = values[index] + recursion(values, weights, index - 1, capacityLeft - weights[index]);
    }

    return max(not_pick, pick);

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) recursion stack space 
}

int memoize(vector<int>& values, vector<int>& weights, int index, int capacityLeft, vector<vector<int>>& dp) {
    if (capacityLeft == 0) return 0;
    if (index == 0) {
        if (capacityLeft >= weights[index]) return values[index];
        return 0;
    }

    if (dp[index][capacityLeft] != -1) return dp[index][capacityLeft];

    int not_pick = memoize(values, weights, index - 1, capacityLeft, dp);
    int pick = 0;
    if (capacityLeft >= weights[index]) {
        pick = values[index] + memoize(values, weights, index - 1, capacityLeft - weights[index], dp);
    }

    return dp[index][capacityLeft] = max(not_pick, pick);

    // Complexity analysis 
    // Time : O(2*N) 
    // Space : O(N) recursion stack space + O(N * Capacity) for memoize 
}

int tabulation(vector<int>& values, vector<int>& weights, int N, int capacity) {
    // index -> 0 - N 
    // weights -> 0 -> capacity

    vector<vector<int>> dp(N, vector<int>(capacity + 1, 0));

    for (int cap = 0; cap <= capacity; cap++) {
        if (weights[0] <= cap) dp[0][cap] = values[0];
    }

    for (int index = 1; index < N; index++) {
        for (int cap = 0; cap <= capacity; cap++) {
            int not_pick = dp[index - 1][cap];
            int pick = 0;
            if (cap >= weights[index]) {
                pick = values[index] + dp[index - 1][cap - weights[index]];
            }

            dp[index][cap] = max(not_pick, pick);
        }
    }

    return dp[N - 1][capacity];

    // Complexity analysis 
    // Time : O(N * capacity) 
    // Space : O(N * capacity) for memoize 
}

int optimise(vector<int>& values, vector<int>& weights, int N, int capacity) {
    // index -> 0 - N 
    // weights -> 0 -> capacity 

    vector<int> dpp(capacity + 1, 0);

    for (int cap = 0; cap <= capacity; cap++) {
        if (weights[0] <= cap) dpp[cap] = values[0];
    }

    for (int index = 1; index < N; index++) {
        vector<int> dpc(capacity + 1, 0);

        for (int cap = 0; cap <= capacity; cap++) {
            int not_pick = dpp[cap];
            int pick = 0;
            if (cap >= weights[index]) {
                pick = values[index] + dpp[cap - weights[index]];
            }

            dpc[cap] = max(not_pick, pick);
        }

        dpp = dpc;
    }

    return dpp[capacity];

    // Complexity analysis 
    // Time : O(N * capacity) 
    // Space : O(capacity) for memoize 
}

// Function to return max value that can be put in knapsack of capacity.
int knapSack(int capacity, vector<int>& values, vector<int>& weights) {
    // code here
    int N = values.size();

    // recursion 
    // return recursion(values, weights, N - 1, capacity);

    // memoize 
    // vector<vector<int>> dp(N, vector<int>(capacity + 1, -1));
    // return memoize(values, weights, N - 1, capacity, dp);

    // tabulation 
    // return tabulation(values, weights, N, capacity);

    // space optimised 
    return optimise(values, weights, N, capacity);
}

void p1() {
    // Problem 1 : Geeksforgeeks 0 - 1 Knapsack Problem - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1 

    int capacity = 5;
    vector<int> values = { 10, 40, 30, 50 };
    vector<int> weights = { 5, 4, 6, 3 };

    int maxVal = knapSack(capacity, values, weights);
    cout << maxVal << endl;
}

int recursionP2(vector<int>& arr, int index, int sum) {
    if (index == 0) {
        int count = 0;
        if (sum == 0) count++;
        if (sum - arr[index] == 0) count++;
        return count;
    }

    int not_pick = recursionP2(arr, index - 1, sum);
    int pick = 0;
    if (arr[index] <= sum) {
        pick = recursionP2(arr, index - 1, sum - arr[index]);
    }

    return (not_pick + pick);

    // Complexity analysis
    // Time : O(2^N)
    // Space : O(N) for stack space
}

int memoizeP2(vector<int>& arr, int index, int sum, vector<vector<int>>& dp) {
    if (index == 0) {
        int count = 0;
        if (sum == 0) count++;
        if (sum - arr[index] == 0) count++;
        return count;
    }

    if (dp[index][sum] != -1) return dp[index][sum];

    int not_pick = memoizeP2(arr, index - 1, sum, dp);
    int pick = 0;
    if (arr[index] <= sum) {
        pick = memoizeP2(arr, index - 1, sum - arr[index], dp);
    }

    return dp[index][sum] = not_pick + pick;

    // Complexity analysis
    // Time : O(2*N)
    // Space : O(N) for stack space + O(N * SUM) for memoization
}

int tabulationP2(vector<int>& arr, int N, int SUM) {
    vector<vector<int>> dp(N, vector<int>(SUM + 1, 0));

    for (int i = 0; i < N; i++) dp[i][0] = 1;
    if (arr[0] <= SUM && arr[0] != 0) dp[0][arr[0]] = 1;
    if (arr[0] == 0) dp[0][0] = 2;

    for (int i = 1; i < N; i++) {
        for (int s = 0; s <= SUM; s++) {
            int not_pick = dp[i - 1][s];
            int pick = 0;
            if (arr[i] <= s) pick = dp[i - 1][s - arr[i]];

            dp[i][s] = (not_pick + pick);
        }
    }

    return dp[N - 1][SUM];

    // Complexity analysis
    // Time : O(N*SUM)
    // Space : O(N * SUM) for memoization
}

int optimiseP2(vector<int>& arr, int N, int SUM) {
    vector<int> dp(SUM + 1, 0);
    vector<int> dpc(SUM + 1);

    dp[0] = dpc[0] = 1;
    if (arr[0] <= SUM && arr[0] != 0) dp[arr[0]] = 1;
    if (arr[0] == 0) dp[0] = 2;

    for (int i = 1; i < N; i++) {
        for (int s = 0; s <= SUM; s++) {
            int not_pick = dp[s];
            int pick = 0;
            if (arr[i] <= s) pick = dp[s - arr[i]];

            dpc[s] = (pick + not_pick);
        }

        dp = dpc;
    }

    return dp[SUM];

    // Complexity analysis
    // Time : O(N*SUM)
    // Space : O(SUM) for memoization
}

int perfectSum(vector<int>& arr, int n, int sum) {
    // Your code goes here

    // recursion
    // return recursionP2(arr, n - 1, sum);

    // memoize
    // vector<vector<int>> dp(n, vector<int>(sum+1, -1));
    // return memoizeP2(arr, n - 1, sum, dp);

    // tabulation
    // return tabulationP2(arr, n, sum);

    // space optimises
    return optimiseP2(arr, n, sum);
}

int countPartitions(int n, int d, vector<int>& arr) {
    // Code here
    int tsum = accumulate(arr.begin(), arr.end(), 0);

    if (((tsum - d) < 0) || ((tsum - d) & 1)) return 0;

    return perfectSum(arr, n, (tsum - d) / 2);
}

int findTargetSumWays(vector<int>& nums, int target) {
    int N = nums.size();
    return countPartitions(N, target, nums);
}

void p2() {
    // Problem 2 : Leetcode 494. Target Sum - https://leetcode.com/problems/target-sum/description/

    vector<int> nums = { 1,1,1,1,1 };
    int target = 2;

    int ways = findTargetSumWays(nums, target);
    cout << ways << endl;
}

int main() {
    // Day 15 of DP 

    p1();

    p2();


    return 0;
}