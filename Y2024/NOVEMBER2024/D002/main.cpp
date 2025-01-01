#include <iostream>
#include <vector>

using namespace std;

int climb(int n, vector<int>& dp) {
    if (n < 0) return 0;
    if (n == 0) return dp[n] = 1;
    if (n == 1) return dp[n] = 1;

    if (dp[n] != -1) return dp[n];

    int a1 = climb(n - 1, dp);
    int a2 = climb(n - 2, dp);

    return dp[n] = a1 + a2;
}

int memoization(int n) {
    // ----- memoization ----- 

    // make sure to init dp of proper size (for all possible and considerable inputs)

    vector<int> dp(n + 1, -1);
    return climb(n, dp);

    // Complexity analysis
    // Time : O(2N) 
    // Space : O(N) + O(2N) for stack 
}

int tabulation(int n) {
    // ------- tabulation -------
    if (n <= 3) return n;

    vector<int> dp(n + 1, -1);

    // base - or start
    dp[0] = 1, dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];

    // Complexity analysis
    // Time : O(N) 
    // Space : O(N) 
}

int space_optimization(int n) {
    // ------- space optimization -------
    if (n <= 3) return n;

    int prev2 = 1, prev1 = 1;

    for (int i = 2; i <= n; i++) {
        int curr = prev2 + prev1;
        prev2 = prev1;
        prev1 = curr;
    }

    return prev1;

    // Complexity analysis
    // Time : O(N) 
    // Space : O(1) 
}

int climbStairs(int n) {
    // N = 2
    // s = 0,
    // 0 -> 2 (1)
    // 0 -> 1 -> 2 (1)
    // 0 -> 1 -> 3 (X)
    // 1 + 1 = 2
    // out : 2

    // N = 3
    // s = 0
    // then
    // 0 -> 1
    // 0 -> 2
    // next
    // 0 -> 1 -> 2
    // 0 -> 1 -> 3 (1)
    // 0 -> 2 -> 3 (1)
    // 0 -> 2 -> 4 (X)
    // next
    // 0 -> 1 -> 2 -> 3 (1)
    // 0 -> 1 -> 2 -> 4 (X)

    // 1 + 1 + 1 = 3
    // out : 3

    // return memoization(n);
    // return tabulation(n);
    return space_optimization(n);
}

void p1() {
    // Problem 1 : Leetcode 70. Climbing Stairs - 
    // https://leetcode.com/problems/climbing-stairs/ 
    // Geeksforgeeks - 
    // https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1 

    int ways = climbStairs(5);

    cout << ways << endl;
}

int __recursion(vector<int>& costs, int index) {
    // ---- simple recursion ----
    if (index >= costs.size()) return 0;

    int a1 = costs[index] + __recursion(costs, index + 1);
    int a2 = costs[index] + __recursion(costs, index + 2);

    return min(a1, a2);
}

int recursion(vector<int>& costs) {
    // ---- simple recursion ----
    return min(__recursion(costs, 0), __recursion(costs, 1));

    // Complexity analysis 
    // Time : O(2 ^ N)
    // Space : O(N) stack space 
}

int __memoization(vector<int>& costs, int index, vector<int>& dp) {
    // ---- memoization ----
    if (index >= costs.size()) return 0;
    if (dp[index] != -1) return dp[index];

    int a1 = costs[index] + __memoization(costs, index + 1, dp);
    int a2 = costs[index] + __memoization(costs, index + 2, dp);

    return dp[index] = min(a1, a2);
}

int memoization(vector<int>& costs) {
    // ---- memoization ---- 

    int N = costs.size();
    vector<int> dp(N + 1, -1);
    return min(__memoization(costs, 0, dp), __memoization(costs, 1, dp));

    // Complexity analysis 
    // Time : O(2N) 
    // Space : O(N) + O(N) for stack 
}

int tabulation(vector<int> dp) {
    // ---- tabulation ---- 

    int N = dp.size();

    for (int i = 2; i < N; i++) {
        dp[i] = dp[i] + min(dp[i - 1], dp[i - 2]);
    }

    return min(dp[N - 1], dp[N - 2]);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(N) 
}

int space_optimization(vector<int>& costs) {
    // ---- tabulation ---- 

    int N = costs.size();
    int p2 = costs[0], p1 = costs[1];

    for (int i = 2; i < N; i++) {
        int curr = costs[i] + min(p2, p1);
        p2 = p1;
        p1 = curr;
    }

    return min(p2, p1);

    // Complexity analysis 
    // Time : O(N) 
    // Space : O(1) 
}

int minCostClimbingStairs(vector<int>& costs) {
    // recursion 
    // return recursion(costs);

    // memoization 
    // return memoization(costs);

    // tabulation 
    // return tabulation(costs);

    // space optimization 
    return space_optimization(costs);
}

void p2() {
    // Problem 2 : Leetcode 746. Min Cost Climbing Stairs - 
    // https://leetcode.com/problems/min-cost-climbing-stairs/ 

    vector<int> costs = { 1,100,1,1,100,1,1,1,100,1,1,100,1,100,1,1,100,1,1,1,100,1,1,100,1,1,100,1,1,1,100,1,1,100,1 };
    int cost = minCostClimbingStairs(costs);

    cout << cost << endl;
}


int main() {
    // Day 2 of DP 

    p1();

    p2();


    return 0;
}