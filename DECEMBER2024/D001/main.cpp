#include <bits/stdc++.h>

using namespace std;

vector<int> nextSmallRight(vector<int>& arr, int n) {
    vector<int> out(n, n - 1);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top() - 1;
        stk.push(i);
    }

    return out;
}

vector<int> nextSmallLeft(vector<int>& arr, int n) {
    vector<int> out(n, 0);
    stack<int> stk;

    for (int i = 0; i < n; i++) {
        while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top() + 1;
        stk.push(i);
    }

    return out;
}

int largestHistogramRectangleArea(vector<int>& heights) {
    // ---- OLD CODE ---- 
    int n = heights.size();
    int ar = 0;
    vector<int> ns_l = nextSmallLeft(heights, n);
    vector<int> ns_r = nextSmallRight(heights, n);

    for (int i = 0; i < n; i++) {
        int e = heights[i], r = ns_r[i], l = ns_l[i];

        int ar_temp = (r - l + 1) * e;
        ar = max(ar, ar_temp);
    }

    return ar;
}

int solve(vector<vector<char>>& matrix) {
    int N = matrix.size(), M = matrix[0].size();

    vector<int> dp(M, 0);

    int marea = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (matrix[i][j] == '1') {
                dp[j] = dp[j] + 1;
            }
            else {
                dp[j] = 0;
            }
        }

        // get max histo area 
        int harea = largestHistogramRectangleArea(dp);
        marea = max(marea, harea);
    }

    return marea;

    // Complexity analysis 
    // Time : O(N*M) ~ 
    // Space : O(M) ~ 
}

int maximalRectangle(vector<vector<char>>& matrix) {
    return solve(matrix);
}

void p1() {
    // Problem 1 : Leetcode 85. Maximal Rectangle - https://leetcode.com/problems/maximal-rectangle/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/max-rectangle/1 

    vector<vector<char>> matrix = {
        {'1','0','1','0','0'},
        {'1','0','1','1','1'},
        {'1','1','1','1','1'},
        {'1','0','0','1','0'}
    };

    int marea = maximalRectangle(matrix);
    cout << marea << endl;
}

int countSquares(vector<vector<int>>& matrix) {
    int N = matrix.size(), M = matrix[0].size();

    vector<vector<int>> dp(N, vector<int>(M, 0));

    // first row & first col 
    for (int j = 0; j < M; j++) dp[0][j] = matrix[0][j];
    for (int i = 0; i < N; i++) dp[i][0] = matrix[i][0];

    for (int i = 1; i < N; i++) {
        for (int j = 1; j < M; j++) {
            if (matrix[i][j] == 1) {
                int bound = min(min(dp[i - 1][j], dp[i - 1][j - 1]), dp[i][j - 1]);
                dp[i][j] = 1 + bound;
            }
        }
    }

    int tsum = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) tsum += dp[i][j];
    }

    return tsum;

    // Complexity analysis 
    // Time : O(2*N*M) 
    // Space : O(N*M) 
}

void p2() {
    // Problem 2 : Leetcode 1277. Count Square Submatrices with All Ones - https://leetcode.com/problems/count-square-submatrices-with-all-ones/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/count-square-submatrices-with-all-ones/0 

    vector<vector<int>> matrix = { {0,1,1,1}, {1,1,1,1}, {0,1,1,1} };

    int sq = countSquares(matrix);
    cout << sq << endl;
}


int main() {
    // Day 1 of December 

    p1();

    p2();


    return 0;
}