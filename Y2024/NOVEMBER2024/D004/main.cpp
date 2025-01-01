#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int recursion(vector<int>& arr, int k, int index) {
    if (index == 0) return 0;

    int min_cost = INT_MAX;

    for (int i = 1; i <= k; i++) {
        if (index - i < 0) break;

        int cost = recursion(arr, k, index - i) + abs(arr[index] - arr[index - i]);
        min_cost = min(min_cost, cost);
    }

    return min_cost;
}

int memoization(vector<int>& arr, int k, int index, vector<int>& dp) {
    if (index == 0) return 0;
    if (dp[index] != -1) return dp[index];

    int min_cost = INT_MAX;

    for (int i = 1; i <= k; i++) {
        if (index - i < 0) break;

        int cost = memoization(arr, k, index - i, dp) + abs(arr[index] - arr[index - i]);
        min_cost = min(min_cost, cost);
    }

    return dp[index] = min_cost;
}

int tabulation(vector<int>& arr, int k) {
    int N = arr.size();

    vector<int> dp(N + 1, 0);

    for (int i = 1; i < arr.size(); i++) {
        int min_energy = INT_MAX;

        for (int j = 1; j <= k; j++) {
            if (i - j >= 0) {
                // valid index 

                int energy = dp[i - j] + abs(arr[i] - arr[i - j]);
                min_energy = min(min_energy, energy);
            }
        }

        dp[i] = min_energy;
    }

    return dp[N - 1];
}

int minimizeCost(int k, vector<int>& arr) {
    // Code here
    int N = arr.size();

    // recursion 
    // return recursion(arr, k, N - 1);

    // memoization 
    // vector<int> dp(N + 1, -1);
    // return memoization(arr, k, N - 1, dp);

    // tabulation 
    return tabulation(arr, k);
}

static void p1() {
    // Problem 1 : Geeksforgeeks Minimal Cost - 
    // https://www.geeksforgeeks.org/problems/minimal-cost/1 

    int k = 3;
    vector<int> arr = { 10, 30, 40, 50, 20 };

    int cost = minimizeCost(k, arr);
    cout << cost << endl;
}

int __recursion(vector<int>& nums, int index) {
    if (index >= nums.size()) return 0;

    int pick = nums[index] + __recursion(nums, index + 2);
    int not_pick = __recursion(nums, index + 1);

    return max(pick, not_pick);
}

int recursion(vector<int>& nums) {
    // recursion 
    int n = nums.size();
    if (n == 1) return nums[0];

    vector<int> temp1, temp2;
    for (int i = 0; i < n; i++) {
        if (i != 0) {
            temp1.push_back(nums[i]);
        }
        if (i != n - 1) {
            temp2.push_back(nums[i]);
        }
    }

    return max(__recursion(temp1, 0), __recursion(temp2, 0));
}

int __memoization(vector<int>& nums, int index, vector<int>& dp) {
    if (index >= nums.size()) return 0;
    if (dp[index] != -1) return dp[index];

    int pick = nums[index] + __memoization(nums, index + 2, dp);
    int not_pick = __memoization(nums, index + 1, dp);

    return dp[index] = max(pick, not_pick);
}

int memoization(vector<int>& nums) {
    // recursion 
    int n = nums.size();
    if (n == 1) return nums[0];

    vector<int> temp1, temp2;
    for (int i = 0; i < n; i++) {
        if (i != 0) {
            temp1.push_back(nums[i]);
        }
        if (i != n - 1) {
            temp2.push_back(nums[i]);
        }
    }

    vector<int> dp1(n + 1, -1);
    vector<int> dp2(n + 1, -1);

    return max(__memoization(temp1, 0, dp1), __memoization(temp2, 0, dp2));

    // Complexity analysis 
    // Time : O(N) + O(2N) 
    // Space : O(2N) + O(2N) + O(N) 
}

int rob(vector<int>& nums) {
    // recursion 
    // return recursion(nums);

    // memoization 
    return memoization(nums);
}

static void p2() {
    // Problem 2 : Leetcode 213. House Robber II - 
    // https://leetcode.com/problems/house-robber-ii/ 
    // Geeksforgeeks - 
    // https://www.geeksforgeeks.org/problems/house-robber-ii/0 

    // vector<int> nums = { 2, 3, 2 };
    vector<int> nums = { 2, 3, 5 };
    int loot = rob(nums);
}


int main() {
    // Day 4 of DP 

    p1();

    p2();


    return 0;
}