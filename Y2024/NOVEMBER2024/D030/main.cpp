#include <bits/stdc++.h>

using namespace std;

class Problem1 {
private:
    int MODO = 1003;

    int recursion(string& s, int i, int j, char need) {
        if (i > j) return 0;
        if (i == j) return s[i] == need;

        int count = 0;

        for (int mid = i + 1; mid <= j - 1; mid += 2) {
            int lpt = recursion(s, i, mid - 1, 'T');
            int lpf = recursion(s, i, mid - 1, 'F');

            int rpt = recursion(s, mid + 1, j, 'T');
            int rpf = recursion(s, mid + 1, j, 'F');

            char opernd = s[mid];

            if (opernd == '&') {
                // T&T=T, T&F=F, F&T=F, F&F=F 
                if (need == 'T') {
                    count = (count + ((lpt * rpt) % MODO)) % MODO;
                }
                else {
                    count = (count + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO) + ((lpf * rpf) % MODO)) % MODO;
                }
            }
            else if (opernd == '|') {
                // T|T=T, T|F=T, F|T=T, F|F=F 
                if (need == 'T') {
                    count = (count + ((lpt * rpt) % MODO) + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO)) % MODO;
                }
                else {
                    count = (count + ((lpf * rpf) % MODO)) % MODO;
                }
            }
            else {
                // T^T=F, T^F=T, F^T=T, F^F=F 
                if (need == 'T') {
                    count = (count + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO)) % MODO;
                }
                else {
                    count = (count + ((lpt * rpt) % MODO) + ((lpf * rpf) % MODO)) % MODO;
                }
            }
        }

        return count;

        // Complexity analysis 
        // Time : O(N * 4^N) 
        // Space : O(N) stack 
    }

    int memoize(string& s, int i, int j, char need, vector<vector<vector<int>>>& dp) {
        if (i > j) return 0;
        if (i == j) return s[i] == need;

        if (dp[i][j][need == 'T'] != -1) return dp[i][j][need == 'T'];

        int count = 0;

        for (int mid = i + 1; mid <= j - 1; mid += 2) {
            int lpt = memoize(s, i, mid - 1, 'T', dp);
            int lpf = memoize(s, i, mid - 1, 'F', dp);

            int rpt = memoize(s, mid + 1, j, 'T', dp);
            int rpf = memoize(s, mid + 1, j, 'F', dp);

            char opernd = s[mid];

            if (opernd == '&') {
                // T&T=T, T&F=F, F&T=F, F&F=F 
                if (need == 'T') {
                    count = (count + ((lpt * rpt) % MODO)) % MODO;
                }
                else {
                    count = (count + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO) + ((lpf * rpf) % MODO)) % MODO;
                }
            }
            else if (opernd == '|') {
                // T|T=T, T|F=T, F|T=T, F|F=F 
                if (need == 'T') {
                    count = (count + ((lpt * rpt) % MODO) + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO)) % MODO;
                }
                else {
                    count = (count + ((lpf * rpf) % MODO)) % MODO;
                }
            }
            else {
                // T^T=F, T^F=T, F^T=T, F^F=F 
                if (need == 'T') {
                    count = (count + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO)) % MODO;
                }
                else {
                    count = (count + ((lpt * rpt) % MODO) + ((lpf * rpf) % MODO)) % MODO;
                }
            }
        }

        return dp[i][j][need == 'T'] = count;

        // Complexity analysis 
        // Time : O(N * N * N) 
        // Space : O(N) stack + O(N*N*2) memory space 
    }

    int tabulation(string& s, int N) {
        vector<vector<vector<int>>> dp(N, vector<vector<int>>(N, vector<int>(2, -1))); // F:0, T:1

        // base
        // case 1 handled 

        // case 2 
        for (int a = 0; a < N; a++) {
            dp[a][a][0] = s[a] == 'F';
            dp[a][a][1] = s[a] == 'T';
        }

        // recurrence 
        for (int i = N - 1; i >= 0; i--) {
            for (int j = i + 1; j <= N - 1; j++) {
                int countT = 0;
                int countF = 0;

                for (int mid = i + 1; mid <= j - 1; mid += 2) {
                    int lpt = dp[i][mid - 1][1];
                    int lpf = dp[i][mid - 1][0];

                    int rpt = dp[mid + 1][j][1];
                    int rpf = dp[mid + 1][j][0];

                    char opernd = s[mid];

                    if (opernd == '&') {
                        // T&T=T, T&F=F, F&T=F, F&F=F 
                        countT = (countT + ((lpt * rpt) % MODO)) % MODO;
                        countF = (countF + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO) + ((lpf * rpf) % MODO)) % MODO;
                    }
                    else if (opernd == '|') {
                        // T|T=T, T|F=T, F|T=T, F|F=F 
                        countT = (countT + ((lpt * rpt) % MODO) + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO)) % MODO;
                        countF = (countF + ((lpf * rpf) % MODO)) % MODO;
                    }
                    else {
                        // T^T=F, T^F=T, F^T=T, F^F=F 
                        countT = (countT + ((lpt * rpf) % MODO) + ((lpf * rpt) % MODO)) % MODO;
                        countF = (countF + ((lpt * rpt) % MODO) + ((lpf * rpf) % MODO)) % MODO;
                    }
                }

                dp[i][j][0] = countF;
                dp[i][j][1] = countT;
            }
        }

        // return 
        return dp[0][N - 1][1];

        // Complexity analysis 
        // Time : O(N * N * N) 
        // Space : O(N * N * 2) memory 
    }

public:
    int countWays(int N, string s) {
        // code here

        // recursion 
        // return recursion(s, 0, N-1, 'T');

        // memoization 
        // vector<vector<vector<int>>> dp(N, vector<vector<int>>(N, vector<int>(2, -1))); // F:0, T:1
        // return memoize(s, 0, N-1, 'T', dp);

        // tabulation 
        return tabulation(s, N);
    }
};

void p1() {
    // Problem 1 : Geeksforgeeks Boolean Parenthesization - https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1 

    int N = 7;
    string s = "T|T&F^T";
    int w = Problem1().countWays(N, s);
    cout << w << endl;
}

class Problem2 {
private:
    bool isPalindrome(string& s, int i, int j) {
        while (i < j) {
            if (s[i++] != s[j--]) return false;
        }
        return true;
    }

    int recursion(string& s, int N, int i) {
        if (i == N) return 0;

        int minc = INT_MAX;

        for (int p = i; p < N; p++) {
            if (isPalindrome(s, i, p)) {
                int cuts = 1 + recursion(s, N, p + 1);
                minc = min(minc, cuts);
            }
        }

        return minc;

        // Complexity analysis 
        // Time : O(N^N) 
        // Space : O(N) stack space 
    }

    int memoize(string& s, int N, int i, vector<int>& dp) {
        if (i == N) return 0;

        if (dp[i] != -1) return dp[i];

        int minc = INT_MAX;

        for (int p = i; p < N; p++) {
            if (isPalindrome(s, i, p)) {
                int cuts = 1 + memoize(s, N, p + 1, dp);
                minc = min(minc, cuts);
            }
        }

        return dp[i] = minc;

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N) stack space + O(N) memory 
    }

    int tabulation(string& s, int N) {
        vector<int> dp(N + 1, 0);

        // base - dp[N] = 0;

        // recurrence 
        for (int i = N - 1; i >= 0; i--) {
            int minc = INT_MAX;

            for (int p = i; p < N; p++) {
                if (isPalindrome(s, i, p)) {
                    int cuts = 1 + dp[p + 1];
                    minc = min(minc, cuts);
                }
            }

            dp[i] = minc;
        }

        // return 
        return dp[0] - 1; // -1 is to exclude last cut 

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N) memory 
    }

public:
    int minCut(string s) {
        int N = s.length();

        // start with recursion 
        // return recursion(s, N, 0) - 1;

        // memoization 
        // vector<int> dp(N, -1);
        // return memoize(s, N, 0, dp) - 1;

        // tabulation 
        return tabulation(s, N);
    }
};

void p2() {
    // Problem 2 : Leetcode 132. Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/palindromic-patitioning4845/1 

    string s = "aaaaa";
    int mc = Problem2().minCut(s);
    cout << mc << endl;
}

class Problem3 {
private:
    long long recursion(vector<int>& arr, int N, int K, int i) {
        if (i == N) return 0;

        long long msum = INT_MIN;

        int cap = min(N, i + K);
        int bada = arr[i];

        for (int p = i; p < cap; p++) {
            bada = max(bada, arr[p]);
            long long sum = (bada * (p - i + 1)) + recursion(arr, N, K, p + 1);
            msum = max(msum, sum);
        }

        return msum;

        // Complexity analysis 
        // Time : O(N^N) ~ 
        // Space : O(N) stack 
    }

    long long memoize(vector<int>& arr, int N, int K, int i, vector<long long>& dp) {
        if (i == N) return 0;

        if (dp[i] != -1) return dp[i];

        long long msum = INT_MIN;

        int cap = min(N, i + K);
        int bada = arr[i];

        for (int p = i; p < cap; p++) {
            bada = max(bada, arr[p]);
            long long sum = (bada * (p - i + 1)) + memoize(arr, N, K, p + 1, dp);
            msum = max(msum, sum);
        }

        return dp[i] = msum;

        // Complexity analysis 
        // Time : O(N*N) ~ 
        // Space : O(N) stack + O(N) memory 
    }

    long long tabulation(vector<int>& arr, int N, int K) {
        vector<long long> dp(N + 1, 0);

        // base - dp[N] = 0;

        // recurrene 
        for (int i = N - 1; i >= 0; i--) {
            long long msum = INT_MIN;

            int cap = min(N, i + K);
            int bada = arr[i];

            for (int p = i; p < cap; p++) {
                bada = max(bada, arr[p]);
                long long sum = (bada * (p - i + 1)) + dp[p + 1];
                msum = max(msum, sum);
            }

            dp[i] = msum;
        }

        // return 
        return dp[0];

        // Complexity analysis 
        // Time : O(N*N) 
        // Space : O(N) memory 
    }

public:
    int maxSumAfterPartitioning(vector<int>& arr, int K) {
        int N = arr.size();

        // recursion 
        // return recursion(arr, N, K, 0);

        // memoization 
        // vector<long long> dp(N, -1);
        // return memoize(arr, N, K, 0, dp);

        // tabulation 
        return tabulation(arr, N, K);
    }
};

void p3() {
    // Problem 3 : Leetcode 1043. Partition Array for Maximum Sum - https://leetcode.com/problems/partition-array-for-maximum-sum/description/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/partition-array-for-maximum-sum/1 

    int K = 4;
    vector<int> arr = { 1,4,1,5,7,3,6,1,9,9,3 };

    int msum = Problem3().maxSumAfterPartitioning(arr, K);
    cout << msum << endl;
}


int main() {
    // Day 30 of DP 

    p1();

    p2();

    p3();


    return 0;
}