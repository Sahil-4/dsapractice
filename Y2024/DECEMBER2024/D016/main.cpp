#include <bits/stdc++.h>

using namespace std;

class Problem1 {
private:
    int recursion(vector<int>& nums, int index) {
        if (index >= nums.size()) return 0;

        int not_pick = recursion(nums, index + 1);
        int pick = nums[index] + recursion(nums, index + 2);

        return max(pick, not_pick);

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) 
    }

    int memoize(vector<int>& nums, int index, vector<int>& dp) {
        if (index >= nums.size()) return 0;

        if (dp[index] != -1) return dp[index];

        int not_pick = memoize(nums, index + 1, dp);
        int pick = nums[index] + memoize(nums, index + 2, dp);

        return dp[index] = max(pick, not_pick);

        // Complexity analysis 
        // Time : O(2*N) 
        // Space : O(N) 
    }

    int tabulation(vector<int>& nums) {
        vector<int> dp(nums.size() + 2, 0);

        for (int i = nums.size() - 1; i >= 0; i--) {
            int npick = dp[i + 1];
            int pick = nums[i] + dp[i + 2];
            dp[i] = max(npick, pick);
        }

        return dp[0];

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(N) 
    }

    int solve(vector<int>& nums) {
        // if there is only one house 
        if (nums.size() == 1) return nums[0];

        // create two arrays 
        // in a1 put 0th element but not (n-1)th element 
        // in a2 put (n-1)th element but not 0th element 

        vector<int> a1, a2;
        for (int i = 0, n = nums.size(); i < n; i++) {
            if (i != 0) a1.push_back(nums[i]);
            if (i != n - 1) a2.push_back(nums[i]);
        }

        // recursion 
        // return max(recursion(a1, 0), recursion(a2, 0));

        // memoize 
        // vector<int> dp1(nums.size(), -1), dp2(nums.size(), -1);
        // return max(memoize(a1, 0, dp1), memoize(a2, 0, dp2));

        // tabulation 
        return max(tabulation(a1), tabulation(a2));

        // as we are calling every function twice time complexity will be multiplied by 2 
        // but again it will not affect much as we are calling functions one after another 
    }

public:
    int rob(vector<int> nums) {
        // [2,3,2] 
        // 2 -> 
        // 3 -> 
        // 2 -> 
        // max is 3 

        // [1,2,3,1]
        // 1 -> 3 -> total 4 
        // 2 -> 1 total 3 
        // 3 -> 1 total 4 
        // 1 -> 2 total 3 
        // max is 4 

        return solve(nums);
    }
};

void p1() {
    // Problem 1 : Leetcode 213. House Robber II - https://leetcode.com/problems/house-robber-ii/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/house-robber-ii/0 

    cout << Problem1().rob({ 2, 4, 6 }) << endl;
    cout << Problem1().rob({ 2, 2, 6 }) << endl;
    cout << Problem1().rob({ 2, 2, 6, 5 }) << endl;
}

class Problem2 {

private:
    int recursion(vector<vector<int>>& triangle, int l, int i) {
        if (l == triangle.size()) return 0;

        int bb = recursion(triangle, l + 1, i);
        int db = recursion(triangle, l + 1, i + 1);
        int out = triangle[l][i] + min(bb, db);

        return out;

        // Complexity analysis 
        // Time : O(2^L) 
        // Space : O(L) 
    }

    int memoize(vector<vector<int>>& triangle, int l, int i, vector<vector<int>>& dp) {
        if (l == triangle.size()) return 0;

        if (dp[l][i] != -1) return dp[l][i];

        int bb = memoize(triangle, l + 1, i, dp);
        int db = memoize(triangle, l + 1, i + 1, dp);
        int out = triangle[l][i] + min(bb, db);

        return dp[l][i] = out;

        // Complexity analysis 
        // Time : O(2*2*L) 
        // Space : O(L) 
    }

    int tabulation(vector<vector<int>>& triangle, int n) {
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));

        for (int l = n - 1; l >= 0; l--) {
            for (int i = l; i >= 0; i--) {
                int bb = dp[l + 1][i];
                int db = dp[l + 1][i + 1];
                int out = triangle[l][i] + min(bb, db);
                dp[l][i] = out;
            }
        }

        return dp[0][0];

        // Complexity analysis 
        // Time : O(2*n*n) 
        // Space : O(n*n) 
    }

public:
    int minimumTotal(vector<vector<int>> triangle) {
        // recursion 
        // return recursion(triangle, 0, 0);

        // memoize 
        // vector<vector<int>> dp(triangle.size(), vector<int>(triangle.size(), -1));
        // return memoize(triangle, 0, 0, dp);

        // tabulation 
        return tabulation(triangle, triangle.size());
    }
};

void p2() {
    // Problem 2 : Leetcode 120. Triangle - https://leetcode.com/problems/triangle/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/triangle-path-sum/1 

    cout << Problem2().minimumTotal({ {2}, {1,4},{2,4,6} }) << endl;
}


int main() {
    // Day 16 of December - Revisiting DP 

    p1();

    p2();


    return 0;
}