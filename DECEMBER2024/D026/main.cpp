#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int recursion(vector<int>& arr, int i, int j) {
        if (i == j) return 0;

        int mini = INT_MAX;

        for (int k = i; k < j; k++) {
            int l_ops = recursion(arr, i, k);
            int r_ops = recursion(arr, k + 1, j);
            int t_ops = arr[i - 1] * arr[k] * arr[j];

            int sum = t_ops + l_ops + r_ops;
            mini = min(mini, sum);
        }

        return mini;

        // Complexity analysis 
        // Time : O(2^N * N) 
        // Space : O(N) stack 
    }

    int memoize(vector<int>& arr, int i, int j, vector<vector<int>>& dp) {
        if (i >= j) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        int mini = INT_MAX;

        for (int k = i; k < j; k++) {
            int l_ops = memoize(arr, i, k, dp);
            int r_ops = memoize(arr, k + 1, j, dp);
            int t_ops = arr[i - 1] * arr[k] * arr[j];

            int sum = t_ops + l_ops + r_ops;
            mini = min(mini, sum);
        }

        return dp[i][j] = mini;

        // Complexity analysis 
        // Time : O(2*N*N) 
        // Space : O(N) stack + O(N*N) memory 
    }

    int tabulation(vector<int>& arr) {
        int N = arr.size();
        vector<vector<int>> dp(N, vector<int>(N, 0));

        for (int i = N - 1; i >= 1; i--) {
            for (int j = 1; j <= N - 1; j++) {
                if (i >= j) continue;

                int mini = INT_MAX;

                for (int k = i; k < j; k++) {
                    int l_ops = dp[i][k];
                    int r_ops = dp[k + 1][j];
                    int t_ops = arr[i - 1] * arr[k] * arr[j];

                    int sum = t_ops + l_ops + r_ops;
                    mini = min(mini, sum);
                }

                dp[i][j] = mini;
            }
        }

        return dp[1][N - 1];

        // Complexity analysis 
        // Time : O(N*N*N) 
        // Space : O(N*N) memory 
    }

public:
    int matrixMultiplication(vector<int> arr) {
        // code here 

        // return recursion(arr, 1, N-1);

        // return memoize(arr, 1, N-1, dp);

        return tabulation(arr);
    }
};

void p1() {
    // Problem 1 : Geeksforgeeks Matrix Chain Multiplication - https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1 

    cout << Problem1().matrixMultiplication({ 10, 20 }) << endl;
    cout << Problem1().matrixMultiplication({ 10, 20, 30 }) << endl;
    cout << Problem1().matrixMultiplication({ 10, 20, 30,10,20 }) << endl;
}

class Problem2 {
    int recursion(vector<int>& cuts, int i, int j) {
        if (i > j) return 0;

        int mcost = INT_MAX;

        for (int k = i; k <= j; k++) {
            int lc = recursion(cuts, i, k - 1);
            int rc = recursion(cuts, k + 1, j);
            int tc = cuts[j + 1] - cuts[i - 1];

            int sum = lc + rc + tc;
            mcost = min(mcost, sum);
        }

        return mcost;

        // Complexity analysis 
        // Time : O(2^N * N) ~ 
        // Space : O(N) 
    }

    int memoize(vector<int>& cuts, int i, int j, vector<vector<int>>& dp) {
        if (i > j) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        int mcost = INT_MAX;

        for (int k = i; k <= j; k++) {
            int lc = memoize(cuts, i, k - 1, dp);
            int rc = memoize(cuts, k + 1, j, dp);
            int tc = cuts[j + 1] - cuts[i - 1];

            int sum = lc + rc + tc;
            mcost = min(mcost, sum);
        }

        return dp[i][j] = mcost;

        // Complexity analysis 
        // Time : O(2*N*N) ~ 
        // Space : O(N) + O(N*N) memory 
    }

    int tabulation(vector<int>& cuts, int N) {
        vector<vector<int>> dp(N + 2, vector<int>(N + 2, 0));

        for (int i = N; i >= 1; i--) {
            for (int j = 1; j <= N; j++) {
                if (i > j) continue;

                int mcost = INT_MAX;

                for (int k = i; k <= j; k++) {
                    int lc = dp[i][k - 1];
                    int rc = dp[k + 1][j];
                    int tc = cuts[j + 1] - cuts[i - 1];

                    int sum = lc + rc + tc;
                    mcost = min(mcost, sum);
                }

                dp[i][j] = mcost;
            }
        }

        return dp[1][N];

        // Complexity analysis 
        // Time : O(N*N*N) 
        // Space : O(N*N) memory 
    }

public:
    int minCost(int len, vector<int> cuts) {
        int N = cuts.size();

        cuts.push_back(0);
        cuts.push_back(len);

        sort(cuts.begin(), cuts.end());

        // return recursion(cuts, 1, N);

        // vector<vector<int>> dp(N+1, vector<int>(N+1, -1));
        // return memoize(cuts, 1, N, dp);

        return tabulation(cuts, N);
    }
};

void p2() {
    // Problem 2 : Leetcode 1547. Minimum Cost to Cut a Stick - https://leetcode.com/problems/minimum-cost-to-cut-a-stick/ 

    cout << Problem2().minCost(7, { 1,3,4,5 });
    cout << Problem2().minCost(9, { 5,6,1,4,2 });
}


int main() {
    // Day 26 of December 

    p1();

    p2();


    return 0;
}