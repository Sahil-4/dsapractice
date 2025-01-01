#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Problem1 {
private:
    static bool comparator_sort(string w1, string w2) {
        return w1.length() < w2.length();
    }

    bool diff1(string& w1, string& w2) {
        int n = w1.length(), m = w2.length();
        if (m - n != 1) return false;

        int i = 0, j = 0;
        while (j < m) {
            if (w1[i] != w2[j]) j++;
            else i++, j++;
        }

        return (i == n && j == m);
    }

    int recursion(vector<string>& words, int& N, int index, int prev) {
        if (index == N) return 0;

        int not_pick = recursion(words, N, index + 1, prev);
        int pick = 0;
        if ((prev == -1) || diff1(words[prev], words[index])) pick = 1 + recursion(words, N, index + 1, index);

        return max(not_pick, pick);

        // Complexity analysis 
        // Time : O(2^N) * O(str_len) 
        // Space : O(N) 
    }

    int memoization(vector<string>& words, int& N, int index, int prev, vector<vector<int>>& dp) {
        if (index == N) return 0;

        if (dp[index][prev + 1] != -1) return dp[index][prev + 1];

        int not_pick = memoization(words, N, index + 1, prev, dp);
        int pick = 0;
        if ((prev == -1) || diff1(words[prev], words[index])) pick = 1 + memoization(words, N, index + 1, index, dp);

        return dp[index][prev + 1] = max(not_pick, pick);

        // Complexity analysis 
        // Time : O(2*N) * O(str_len) 
        // Space : O(N) + O(N*N) for memory 
    }

    int tabulation(vector<string>& words, int& N) {
        vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));

        // base case - handled 

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            for (int prev = index - 1; prev >= -1; prev--) {
                int not_pick = dp[index + 1][prev + 1];
                int pick = 0;
                if ((prev == -1) || diff1(words[prev], words[index])) pick = 1 + dp[index + 1][index + 1];

                dp[index][prev + 1] = max(not_pick, pick);
            }
        }

        // return 
        return dp[0][0];

        // Complexity analysis 
        // Time : O(N*N*(str_len)) 
        // Space : O((N + 1) * (N + 1)) for memory 
    }

    int optimise(vector<string>& words, int& N) {
        // vector<vector<int>> dp(N+1, vector<int>(N+1, 0));
        vector<int> dpn(N + 1, 0);

        // recurrence 
        for (int index = N - 1; index >= 0; index--) {
            vector<int> dpc(N + 1, 0);

            for (int prev = index - 1; prev >= -1; prev--) {
                int not_pick = dpn[prev + 1];
                int pick = 0;
                if ((prev == -1) || diff1(words[prev], words[index])) pick = 1 + dpn[index + 1];

                dpc[prev + 1] = max(not_pick, pick);
            }

            dpn = dpc;
        }

        // return 
        return dpn[0];

        // Complexity analysis 
        // Time : O(N*N*(str_len)) 
        // Space : O(2 * (N + 1)) for memory 
    }

public:
    int longestStrChain(vector<string>& words) {
        int N = words.size();

        // sort words array 
        sort(words.begin(), words.end(), comparator_sort); // N*log(N) 

        // recursion 
        // return recursion(words, N, 0, -1);

        // memoization 
        // vector<vector<int>> dp(N, vector<int>(N, -1));
        // return memoization(words, N, 0, -1, dp);

        // tabulation 
        // return tabulation(words, N);

        // space optimised 
        return optimise(words, N);
    }
};

void p1() {
    // Problem 1 : Leetcode 1048. Longest String Chain - https://leetcode.com/problems/longest-string-chain/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/longest-string-chain/1 

    vector<string> words = { "xbc","pcxbcf","xb","cxbc","pcxbc" };

    int lsc = Problem1().longestStrChain(words);
    cout << lsc << endl;
}

int LongestBitonicSequence(int N, vector<int>& arr) {
    // code here
    vector<int> dp_lis(N, 1);
    vector<int> dp_lds(N, 1);

    for (int index = 0; index < N; index++) {
        for (int prev = index - 1; prev >= 0; prev--) {
            // longest increasing subseq 
            if (arr[prev] < arr[index] && dp_lis[index] < dp_lis[prev] + 1) {
                dp_lis[index] = dp_lis[prev] + 1;
            }
        }
    }

    for (int index = N - 1; index >= 0; index--) {
        for (int next = N - 1; next > index; next--) {
            // longest increasing subseq 
            if (arr[next] < arr[index] && dp_lds[index] < dp_lds[next] + 1) {
                dp_lds[index] = dp_lds[next] + 1;
            }
        }
    }

    int max_seq_len = 0;

    for (int i = 0; i < N; i++) {
        int lis_len = dp_lis[i];
        int lds_len = dp_lds[i];
        int sum = lis_len + lds_len - 1;

        // for strictly bitonic 
        if (lis_len == 1 || lds_len == 1) continue;

        max_seq_len = max(max_seq_len, sum);
    }

    return max_seq_len;

    // Complexity analysis 
    // Time : O(N*N) + O(N*N) + O(N) 
    // Space : O(N) + O(N) 
}

void p2() {
    // Problem 2 : Geeksforgeeks Longest Bitonic subsequence - https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1 

    vector<int> arr = { 1,2,5,4 };

    int len = LongestBitonicSequence(arr.size(), arr);
    cout << len << endl;
}

int findNumberOfLIS(vector<int>& arr) {
    int N = arr.size();

    vector<int> dp_lis(N, 1);
    vector<int> dp_lis_cnt(N, 1);
    int lis_len = 0;

    for (int index = 0; index < N; index++) {
        for (int prev = index - 1; prev >= 0; prev--) {
            if (arr[prev] < arr[index] && dp_lis[index] < dp_lis[prev] + 1) {
                dp_lis[index] = dp_lis[prev] + 1;
                dp_lis_cnt[index] = dp_lis_cnt[prev];
            }
            else if (arr[prev] < arr[index] && dp_lis[index] == dp_lis[prev] + 1) {
                dp_lis_cnt[index] += dp_lis_cnt[prev];
            }
        }

        lis_len = max(lis_len, dp_lis[index]);
    }

    int lis_cnt = 0;
    for (int i = 0; i < N; i++) {
        if (dp_lis[i] == lis_len) {
            lis_cnt += dp_lis_cnt[i];
        }
    }

    return lis_cnt;

    // Complexity analysis 
    // Time : O(N * N) + O(N) 
    // Space : O(N) + O(N) 
}

void p3() {
    // Problem 3 : Leetcode 673. Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/number-of-longest-increasing-subsequence/0 

    vector<int> arr = { 1,2,5,4 };

    int n = findNumberOfLIS(arr);
    cout << n << endl;
}


int main() {
    // Day 27 of DP 

    p1();

    p2();

    p3();


    return 0;
}
