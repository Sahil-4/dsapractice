#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Problem1 {
private:
    int recursion(vector<int>& arr, int& N, int index, int prev) {
        if (index == N) return 0;

        int not_pick = recursion(arr, N, index + 1, prev);
        int pick = 0;
        if (prev == 0 || arr[index] > arr[prev - 1]) {
            pick = 1 + recursion(arr, N, index + 1, index + 1);
        }

        return max(pick, not_pick);

        // Complexity analysis 
        // Time : O(2^N) 
        // Space : O(N) stack space 
    }

    int memoization(vector<int>& arr, int& N, int index, int prev, vector<vector<int>>& dp) {
        if (index == N) return 0;

        if (dp[index][prev] != -1) return dp[index][prev];

        int not_pick = memoization(arr, N, index + 1, prev, dp);
        int pick = 0;
        if (prev == 0 || arr[index] > arr[prev - 1]) {
            pick = 1 + memoization(arr, N, index + 1, index + 1, dp);
        }

        return dp[index][prev] = max(pick, not_pick);

        // Complexity analysis 
        // Time : O(2*2*N) 
        // Space : O(N) stack space + O(N * N+1) for memory 
    }

    int tabulation(vector<int>& arr, int N) {
        vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));

        // base - handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            for (int prev = N - 1; prev >= 0; prev--) {
                int not_pick = dp[index + 1][prev];
                int pick = 0;
                if (prev == 0 || arr[index] > arr[prev - 1]) {
                    pick = 1 + dp[index + 1][index + 1];
                }

                dp[index][prev] = max(pick, not_pick);
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N+1 * N+1) for memory 
    }

    int optimise(vector<int>& arr, int N) {
        vector<int> dpn(N + 1, 0);

        // base - handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            vector<int> dpc(N + 1, 0);

            for (int prev = N - 1; prev >= 0; prev--) {
                int not_pick = dpn[prev];
                int pick = 0;
                if (prev == 0 || arr[index] > arr[prev - 1]) {
                    pick = 1 + dpn[index + 1];
                }

                dpc[prev] = max(pick, not_pick);
            }

            dpn = dpc;
        }

        // return 
        return dpn[0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(2* N+1) for memory 
    }

public:
    int lengthOfLIS(vector<int>& arr) {
        int N = arr.size();

        // recursion 
        // return recursion(arr, N, 0, 0);

        // memoization 
        // vector<vector<int>> dp(N, vector<int>(N+1, -1));
        // return memoization(arr, N, 0, 0, dp);

        // tabulation 
        // return tabulation(arr, N);

        // optimise 
        return optimise(arr, N);
    }
};

void p1() {
    // Problem 1 : Leetcode 300. Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1 

    vector<int> arr = { 10,9,2,5,3,7,101,18 };
    int len = Problem1().lengthOfLIS(arr);
    cout << len << endl;
}

vector<int> tabulation2(vector<int>& arr, int N) {
    // for tracing LIS 
    vector<int> path(N);
    vector<int> dp(N, 1);
    int bada = 0;

    for (int index = 0; index < N; index++) {
        path[index] = index;

        for (int prev = 0; prev < index; prev++) {
            if (arr[prev] < arr[index] && dp[index] < 1 + dp[prev]) {
                dp[index] = 1 + dp[prev];
                path[index] = prev;
            }
        }

        if (dp[index] > dp[bada]) bada = index;
    }

    vector<int> LIS;
    int idx = bada;

    while (path[idx] != idx) {
        LIS.push_back(arr[idx]);
        idx = path[idx];
    }
    LIS.push_back(arr[idx]);

    reverse(LIS.begin(), LIS.end());

    return LIS;

    // Complexity analysis 
    // Time : O(N*N) 
    // Space : O(2N) for memory 
}

void p2() {
    // Problem 2 : Geeksforgeeks Print Longest Increasing Subsequence - https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1 

    vector<int> arr = { 10,9,2,5,3,7,101,18 };
    vector<int> LIS = tabulation2(arr, arr.size());
    for (int i = 0; i < LIS.size(); i++) cout << LIS[i] << endl;
    cout << endl;
}


int main() {
    // Day 25 of DP 

    p1();

    p2();


    return 0;
}