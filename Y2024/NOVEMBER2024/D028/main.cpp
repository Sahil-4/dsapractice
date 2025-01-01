#include <bits/stdc++.h>

using namespace std;

class Problem1 {
private:
    int recursion(vector<int>& arr, int i, int j) {
        if (i == j) return 0;

        int min_oprs = INT_MAX;

        for (int k = i; k < j; k++) {
            int op = arr[i - 1] * arr[k] * arr[j];
            int lp = recursion(arr, i, k);
            int rp = recursion(arr, k + 1, j);

            int oprs = lp + op + rp;

            min_oprs = min(min_oprs, oprs);
        }

        return min_oprs;

        // Complexity analysis 
        // Time : O(2^N * N) 
        // Space : O(N) stack space 
    }

    int memoization(vector<int>& arr, int i, int j, vector<vector<int>>& dp) {
        if (i == j) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        int min_oprs = INT_MAX;

        for (int k = i; k < j; k++) {
            int op = arr[i - 1] * arr[k] * arr[j];
            int lp = memoization(arr, i, k, dp);
            int rp = memoization(arr, k + 1, j, dp);

            int oprs = lp + op + rp;

            min_oprs = min(min_oprs, oprs);
        }

        return dp[i][j] = min_oprs;

        // Complexity analysis 
        // Time : O(2 * N * N) 
        // Space : O(N) stack space + O(N*N) memory 
    }

    int tabulation(vector<int>& arr, int N) {
        vector<vector<int>> dp(N, vector<int>(N, 0));

        // base - already handled 

        for (int i = N - 1; i >= 1; i--) {
            for (int j = i + 1; j <= N - 1; j++) {
                int min_oprs = INT_MAX;

                for (int k = i; k < j; k++) {
                    int op = arr[i - 1] * arr[k] * arr[j];
                    int lp = dp[i][k];
                    int rp = dp[k + 1][j];

                    int oprs = lp + op + rp;

                    min_oprs = min(min_oprs, oprs);
                }

                dp[i][j] = min_oprs;
            }
        }

        return dp[1][N - 1];

        // Complexity analysis 
        // Time : O(N * N * N) 
        // Space : O(N*N) memory 
    }

public:
    int matrixMultiplication(vector<int>& arr) {
        // code here
        int N = arr.size();

        // recursion 
        // return recursion(arr, 1, N-1);

        // memoization 
        // vector<vector<int>> dp(N, vector<int>(N, -1));
        // return memoization(arr, 1, N-1, dp);

        // tabulation 
        return tabulation(arr, N);
    }
};

void p1() {
    // Problem 1 : Geeksforgeeks Matrix Chain Multiplication - https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1 

    vector<int> arr = { 500, 500, 500, 500, 500, 500, 500 };

    int topr = Problem1().matrixMultiplication(arr);
    cout << topr << endl;
}

class Problem2 {
private:
    int recursion(vector<int>& cuts, int i, int j) {
        if (i > j) return 0;

        int mcost = INT_MAX;

        for (int k = i; k <= j; k++) {
            int tcost = cuts[j + 1] - cuts[i - 1];

            int lcost = recursion(cuts, i, k - 1);
            int rcost = recursion(cuts, k + 1, j);

            int cost = tcost + lcost + rcost;
            mcost = min(mcost, cost);
        }

        return mcost;

        // Complexity analysis 
        // Time : O(2^N) ~
        // Space : O(N) stack 
    }

    int memoization(vector<int>& cuts, int i, int j, vector<vector<int>>& dp) {
        if (i > j) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        int mcost = INT_MAX;

        for (int k = i; k <= j; k++) {
            int tcost = cuts[j + 1] - cuts[i - 1];

            int lcost = memoization(cuts, i, k - 1, dp);
            int rcost = memoization(cuts, k + 1, j, dp);

            int cost = tcost + lcost + rcost;
            mcost = min(mcost, cost);
        }

        return dp[i][j] = mcost;

        // Complexity analysis 
        // Time : O(2*N*N) ~ 
        // Space : O(N) stack + O(N+1 * N+1) memory 
    }

    int tabulation(vector<int>& cuts, int N) {
        vector<vector<int>> dp(N + 2, vector<int>(N + 2, 0));

        // base - already handled 

        // recurrence - i, j 
        for (int i = N; i >= 1; i--) {
            for (int j = i; j <= N; j++) {
                int mcost = INT_MAX;

                for (int k = i; k <= j; k++) {
                    int tcost = cuts[j + 1] - cuts[i - 1];

                    int lcost = dp[i][k - 1];
                    int rcost = dp[k + 1][j];

                    int cost = tcost + lcost + rcost;
                    mcost = min(mcost, cost);
                }

                dp[i][j] = mcost;
            }
        }

        // return 
        return dp[1][N];

        // Complexity analysis 
        // Time : O(N*N*N) ~ 
        // Space : O(N+2 * N+2) memory 
    }

public:
    int minCost(int len, vector<int>& cuts) {
        int N = cuts.size();

        cuts.push_back(0); cuts.push_back(len);
        sort(cuts.begin(), cuts.end()); // n * log(n) 

        // recursion 
        // return recursion(cuts, 1, N);

        // memoization 
        // vector<vector<int>> dp(N+1, vector<int>(N+1, -1));
        // return memoization(cuts, 1, N, dp);

        // tabulation 
        return tabulation(cuts, N);
    }
};

void p2() {
    // Problem 2 : Leetcode 1547. Minimum Cost to Cut a Stick - https://leetcode.com/problems/minimum-cost-to-cut-a-stick/ 

    int len = 9;
    vector<int> cuts = { 5,6,1,4,2 };

    int cost = Problem2().minCost(len, cuts);
    cout << cost << endl;
}


int main() {
    // Day 28 of DP 

    p1();

    p2();


    return 0;
}