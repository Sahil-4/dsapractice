#include <bits/stdc++.h>

using namespace std;

int LongestBitonicSequence(int N, vector<int> nums) {
    // code here
    // simple approach - 
    // lis find kro at different position 
    // lds find kro at different position 
    // next find the pair of lis and lds which gives maximum sum 
    // for strictly bitonic just dont pick lis and lds if any of them is of 1 length 

    vector<int> lis_dp(N + 1, 1); // lis ka dp 
    vector<int> lds_dp(N + 1, 1); // lds ka dp 

    // lis ki lengths find kro 
    for (int index = 0; index < N; index++) {
        for (int prev = index - 1; prev >= 0; prev--) {
            if (nums[prev] < nums[index] && lis_dp[index] < lis_dp[prev] + 1) {
                lis_dp[index] = lis_dp[prev] + 1;
            }
        }
    }

    // lds ki lengths find kro 
    for (int index = N - 1; index >= 0; index--) {
        for (int prev = N - 1; prev > index; prev--) {
            if (nums[prev] < nums[index] && lds_dp[index] < lds_dp[prev] + 1) {
                lds_dp[index] = lds_dp[prev] + 1;
            }
        }
    }

    int bitonic_len = 0;

    // now make pair of lis and lds - to create a bitonic subseq 
    for (int i = 0; i < N; i++) {
        int lis_ka_len = lis_dp[i];
        int lds_ka_len = lds_dp[i];

        // strictly bitonic hona chahiye 
        if (lis_ka_len == 1 || lds_ka_len == 1) continue;

        int sum = lis_ka_len + lds_ka_len - 1;
        bitonic_len = max(bitonic_len, sum);
    }

    return bitonic_len;
}

void p1() {
    // Problem 1 : Geeksforgeeks Longest Bitonic subsequence - https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1 

    cout << LongestBitonicSequence(8, { 1, 11, 2, 10, 4, 5, 2, 1 }) << endl;
    cout << LongestBitonicSequence(3, { 10, 20, 30 }) << endl;
}

int findNumberOfLIS(vector<int> nums) {
    int N = nums.size();

    int lis_len = 0; // longest lis ki length 
    vector<int> lis_dp(N + 1, 1); // lis ka dp 
    vector<int> lis_count_dp(N + 1, 1); // lis ke count wala dp 

    for (int index = 0; index < N; index++) {
        for (int prev = index - 1; prev >= 0; prev--) {
            if (nums[prev] < nums[index] && lis_dp[index] < lis_dp[prev] + 1) {
                lis_dp[index] = lis_dp[prev] + 1;
                lis_count_dp[index] = lis_count_dp[prev];
            } else if (nums[prev] < nums[index] && lis_dp[index] == lis_dp[prev] + 1) {
                lis_count_dp[index] += lis_count_dp[prev];
            }
        }

        lis_len = max(lis_len, lis_dp[index]);
    }

    int nlis = 0;
    for (int i = 0; i < N; i++) {
        // agar same length or longest length inc subseq hai to 
        if (lis_dp[i] == lis_len) nlis += lis_count_dp[i];
    }

    return nlis;
}

void p2() {
    // Problem 2 : Leetcode 673. Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/ 

    cout << findNumberOfLIS({ 1,3,5,4,7,2,5,8,12 }) << endl;
}


int main() {
    // Day 25 of December 

    p1();

    p2();


    return 0;
}