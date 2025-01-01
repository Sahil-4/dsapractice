#include <iostream>
#include <vector>

using namespace std;

bool recursion(vector<int>& arr, int N, int t, int i, int sum) {
    if (sum == t) return true;
    if (sum > t || i >= N) return false;

    bool pick = recursion(arr, N, t, i + 1, sum + arr[i]);
    bool not_pick = recursion(arr, N, t, i + 1, sum);

    return pick || not_pick;

    // Complexity analysis 
    // Time : O(2^N) 
    // Space : O(N) recursion stack space 
}

bool memoization(vector<int>& arr, int N, int t, int i, int sum, vector<vector<int>>& dp) {
    if (sum == t) return true;
    if (sum > t || i >= N) return false;

    if (dp[i][sum] != -1) return dp[i][sum];

    bool pick = memoization(arr, N, t, i + 1, sum + arr[i], dp);
    bool not_pick = memoization(arr, N, t, i + 1, sum, dp);

    dp[i][sum] = (pick || not_pick) ? 1 : 0;

    return pick || not_pick;

    // Complexity analysis 
    // Time : O(N * t) 
    // Space : O(N) recursion stack space + O(N * t) for memoization 
}

bool memoization2(vector<int>& arr, int i, int t, vector<vector<int>>& dp) {
    if (t == 0) return true;
    if (i == 0) return (arr[0] == t);

    if (dp[i][t] != -1) return dp[i][t];

    bool not_pick = memoization2(arr, i - 1, t, dp);
    bool pick = false;
    if (arr[i] <= t) {
        pick = memoization2(arr, i - 1, t - arr[i], dp);
    }

    dp[i][t] = (pick || not_pick) ? 1 : 0;

    return dp[i][t];

    // Complexity analysis 
    // Time : O(N * t) 
    // Space : O(N) recursion stack space + O(N * t) for memoization 
}
bool tabulation(vector<int>& arr, int N, int target) {
    vector<vector<bool>> dp(N, vector<bool>(target + 1, 0));

    for (int i = 0; i < N; i++) {
        dp[i][0] = true;
    }
    dp[0][arr[0]] = true;

    for (int i = 1; i < N; i++) {
        for (int t = 1; t <= target; t++) {
            bool not_pick = dp[i - 1][t];
            bool pick = false;
            if (arr[i] <= t) pick = dp[i - 1][t - arr[i]];

            dp[i][t] = not_pick || pick;
        }
    }

    return dp[N - 1][target];

    // Complexity analysis 
    // Time : O(N * target) 
    // Space : O(N * target+1) for memoization 
}

bool optimised(vector<int>& arr, int N, int target) {
    vector<bool> dp(target + 1, 0);

    dp[0] = true;
    dp[arr[0]] = true;

    for (int i = 1; i < N; i++) {
        vector<bool> dpc(target + 1, 0);
        dpc[0] = true;

        for (int t = 1; t <= target; t++) {
            bool not_pick = dp[t];
            bool pick = false;
            if (arr[i] <= t) pick = dp[t - arr[i]];

            dpc[t] = not_pick || pick;
        }

        dp = dpc;
    }

    return dp[target];

    // Complexity analysis 
    // Time : O(N * target) 
    // Space : O(2 * target+1) for memoization 
}

bool isSubsetSum(vector<int>& arr, int target) {
    // code here

    int N = arr.size();

    // recursion 
    // return recursion(arr, N, target, 0, 0);

    // memoization 
    // vector<vector<int>> dp(N, vector<int>(target + 1, -1));
    // return memoization(arr, N, target, 0, 0, dp);

    // memoization 
    // vector<vector<int>> dp(N, vector<int>(target + 1, -1));
    // return memoization2(arr, N - 1, target, dp);

    // tabulation 
    return tabulation(arr, N, target);
}

void p1() {
    // Problem 1 : Geeksforgeeks Subset Sum Problem - https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1 

    vector<int> arr = { 3, 34, 4, 12, 5, 2 };
    int target = 9;

    bool check = isSubsetSum(arr, target);
    cout << check << endl;
}

bool canPartition(vector<int>& arr) {
    int N = arr.size();

    int t_sum = 0;
    for (int i = 0; i < N; i++) t_sum += arr[i];

    // odd sum - cant partition 
    if (t_sum & 1) return false;

    return isSubsetSum(arr, t_sum / 2);
}

void p2() {
    // Problem 2 : Leetcode 416. Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/ 

    vector<int> arr = { 3, 34, 4, 19, 5, 3 };

    bool check = canPartition(arr);
    cout << check << endl;
}

int main() {
    // Day 12 of DP 

    p1();

    p2();


    return 0;
}