#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    // sort_by_length
    static bool sort_by_length(string& s1, string& s2) {
        return s2.length() > s1.length();
    }

    int diff(string& s1, string& s2) {
        // NOTE : s2 should greater then s1 by 1 length 
        if (s2.length() - s1.length() != 1) return 0;

        int diff = 0;
        int p1 = 0, p2 = 0;
        int N = s1.length(), M = s2.length();

        while (p1 < N && p2 < M) {
            if (s1[p1] == s2[p2]) p1++, p2++;
            else diff++, p2++;
            // because s2 is greater then s1 we can (but only) move p2 1 index ahead 
        }

        if (p2 < M) diff++;
        return diff;

        // Complexity analysis 
        // Time : O(M) 
        // Space : O(1) 
    }

    int recursion(vector<string>& words, int index, int prev) {
        if (index >= words.size()) return 0;

        int not_pick = recursion(words, index + 1, prev);
        int pick = 0;
        if ((prev == -1) || (diff(words[prev], words[index]) == 1)) {
            pick = 1 + recursion(words, index + 1, index);
        }

        return max(not_pick, pick);

        // Complexity analysis 
        // Time : O(2^N * N * str_len) 
        // Space : O(N) 
    }

    int memoize(vector<string>& words, int N, int index, int prev, vector<vector<int>>& dp) {
        if (index >= N) return 0;

        if (dp[index][prev + 1] != -1) return dp[index][prev + 1];

        int not_pick = memoize(words, N, index + 1, prev, dp);
        int pick = 0;
        if ((prev == -1) || (diff(words[prev], words[index]) == 1)) pick = 1 + memoize(words, N, index + 1, index, dp);

        return dp[index][prev + 1] = max(not_pick, pick);

        // Complexity analysis 
        // Time : O(2 * ((N * N) * str_len)) 
        // Space : O(N) + O(N*N) memory 
    }

    int tabulation(vector<string>& words) {
        int N = words.size();
        vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));

        for (int index = N - 1; index >= 0; index--) {
            for (int prev = index - 1; prev >= -1; prev--) {
                int not_pick = dp[index + 1][prev + 1];
                int pick = 0;
                if ((prev == -1) || (diff(words[prev], words[index]) == 1)) {
                    pick = 1 + dp[index + 1][index + 1];
                }

                dp[index][prev + 1] = max(not_pick, pick);
            }
        }

        return dp[0][0];

        // Complexity analysis 
        // Time : O(N * N * str_len) 
        // Space : O(N*N) memory 
    }

    int optimise(vector<string>& words) {
        int N = words.size();
        vector<int> dpp(N + 1, 0);

        for (int index = N - 1; index >= 0; index--) {
            vector<int> dpc(N + 1, 0);

            for (int prev = index - 1; prev >= -1; prev--) {
                int not_pick = dpp[prev + 1];
                int pick = 0;
                if ((prev == -1) || (diff(words[prev], words[index]) == 1)) {
                    pick = 1 + dpp[index + 1];
                }

                dpc[prev + 1] = max(not_pick, pick);
            }

            dpp = dpc;
        }

        return dpp[0];

        // Complexity analysis 
        // Time : O(N * N * str_len) 
        // Space : O(2*N) memory 
    }

    int solve(vector<string> words) {
        // O(N) extra space for copying input 
        // N*Log(N) extra time for sorting 

        sort(words.begin(), words.end(), sort_by_length);

        // return recursion(words, 0, -1);

        // int N = words.size();
        // vector<vector<int>> dp(N, vector<int>(N+1, -1));
        // return memoize(words, N, 0, -1, dp);

        // return tabulation(words);

        return optimise(words);
    }

public:
    int longestStrChain(vector<string> words) {
        return solve(words);
    }
};

void p1() {
    // Problem 1 : Leetcode 1048. Longest String Chain - https://leetcode.com/problems/longest-string-chain/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-string-chain/0 

    cout << Problem1().longestStrChain({ "a","b","ba","bca","bda","bdca" }) << endl;
    cout << Problem1().longestStrChain({ "xbc","pcxbcf","xb","cxbc","pcxbc" }) << endl;
}


int main() {
    // Day 24 

    p1();


    return 0;
}