#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(int n) {
        if (n < 0) return 0;
        if (n == 0) return 1;

        // two options 
        int a = recursion(n - 1);
        int b = recursion(n - 2);

        return a + b;

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) stack 
    }

    int memoize(int n, vector<int>& dp) {
        if (n < 0) return 0;
        if (n == 0) return 1;

        if (dp[n] != -1) return dp[n];

        // two options 
        int a = memoize(n - 1, dp);
        int b = memoize(n - 2, dp);

        return dp[n] = (a + b);

        // Complexity analysis 
        // Time : O(2N) 
        // Space : O(N) stack + O(N) memory 
    }

    int tabulation(int n) {
        vector<int> dp(n + 1, 0);

        // base case 
        dp[0] = 1;

        for (int i = 1; i <= n; i++) {
            int a = (i - 1 < 0) ? 0 : dp[i - 1];
            int b = (i - 2 < 0) ? 0 : dp[i - 2];
            dp[i] = (a + b);
        }

        return dp[n];

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N) memory 
    }

    int optimised(int n) {
        // base case 
        int a = 0, b = 1;

        for (int i = 1; i <= n; i++) {
            int t = a + b;
            a = b;
            b = t;
        }

        return b;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

public:
    int climbStairs(int n) {
        // return recursion(n);

        // vector<int> dp(n+1, -1);
        // return memoize(n, dp);

        // return tabulation(n);

        return optimised(n);
    }
};

void p1() {
    // Problem 1 : Leetcode 70. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1 

    cout << Problem1().climbStairs(1) << endl;
    cout << Problem1().climbStairs(2) << endl;
    cout << Problem1().climbStairs(4) << endl;
    cout << Problem1().climbStairs(8) << endl;
    cout << Problem1().climbStairs(15) << endl;
    cout << Problem1().climbStairs(25) << endl;
    cout << Problem1().climbStairs(45) << endl;
}

class Problem2 {
    int recursion(vector<int>& nums, int ci, int pi) {
        if (ci >= nums.size()) return 0;

        // lets take nums[ci] if we can 
        int option_a = 0;
        if (pi == -1 || ci > pi + 1) {
            option_a = nums[ci] + recursion(nums, ci + 1, ci);
        }
        // lets dont take nums[ci] 
        int option_b = recursion(nums, ci + 1, pi);

        return max(option_a, option_b);

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) 
    }

    int memoize(vector<int>& nums, int ci, int pi, vector<vector<int>>& dp) {
        if (ci > nums.size()) return 0;

        if (dp[ci][pi] != -1) return dp[ci][pi];

        // lets take nums[ci] if we can 
        int option_a = 0;
        if (pi == 0 || ci > pi + 1) {
            option_a = nums[ci - 1] + memoize(nums, ci + 1, ci, dp);
        }
        // lets dont take nums[ci] 
        int option_b = memoize(nums, ci + 1, pi, dp);

        return dp[ci][pi] = max(option_a, option_b);

        // Complexity analysis 
        // Time : O(2*N*N) 
        // Space : O(N) 
    }

    int tabulation(vector<int>& nums) {
        int N = nums.size();
        vector<vector<int>> dp(N + 2, vector<int>(N + 2, 0));

        // base case 
        for (int ci = nums.size(); ci >= 1; ci--) {
            for (int pi = nums.size(); pi >= 0; pi--) {
                // lets take nums[ci] if we can 
                int option_a = 0;
                if (pi == 0 || ci > pi + 1) {
                    option_a = nums[ci - 1] + dp[ci + 1][ci];
                }
                // lets dont take nums[ci] 
                int option_b = dp[ci + 1][pi];

                dp[ci][pi] = max(option_a, option_b);
            }
        }

        // return 
        return dp[1][0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N*N) 
    }

    int optimised(vector<int>& nums) {
        int N = nums.size();
        // vector<vector<int>> dp(N+2, vector<int>(N+2, 0));
        vector<int> next(N + 2, 0);

        // base case 
        for (int ci = nums.size(); ci >= 1; ci--) {
            vector<int> curr(N + 2, 0);
            for (int pi = nums.size(); pi >= 0; pi--) {
                // lets take nums[ci] if we can 
                int option_a = 0;
                if (pi == 0 || ci > pi + 1) {
                    option_a = nums[ci - 1] + next[ci];
                }
                // lets dont take nums[ci] 
                int option_b = next[pi];

                curr[pi] = max(option_a, option_b);
            }

            next = curr;
        }

        // return 
        return next[0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N) 
    }

public:
    int rob(vector<int>& nums) {
        // return recursion(nums, 0, -1);

        // int N = nums.size();
        // vector<vector<int>> dp(N+1, vector<int>(N+1, -1));
        // return memoize(nums, 1, 0, dp);

        // return tabulation(nums);

        return optimised(nums);
    }
};

void p2() {
    // Problem 2 : Leetcode 198. House Robber - https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks -  https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1 

    vector<int> nums = { 2,55,7 };
    cout << Problem2().rob(nums) << endl;
}


int main() {
    // Day 14 of February 2025 

    p1();

    p2();


    return 0;
}
