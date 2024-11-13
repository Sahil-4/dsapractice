#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int minimumDifference(vector<int>& nums) {
    int n = nums.size(), res = 0, sum = 0;
    sum = accumulate(nums.begin(), nums.end(), 0);

    int N = n / 2;
    vector<vector<int>> left(N + 1), right(N + 1);

    for (int mask = 0; mask < (1 << N); ++mask) {
        int sz = 0, l = 0, r = 0;
        for (int i = 0; i < N; ++i) {
            if (mask & (1 << i)) {
                sz++;
                l += nums[i];
                r += nums[i + N];
            }
        }
        left[sz].push_back(l);
        right[sz].push_back(r);
    }

    for (int sz = 0; sz <= N; ++sz) {
        sort(right[sz].begin(), right[sz].end());
    }

    res = min(abs(sum - 2 * left[N][0]), abs(sum - 2 * right[N][0]));

    for (int sz = 1; sz < N; ++sz) {
        for (auto& a : left[sz]) {
            int b = (sum - 2 * a) / 2, rsz = N - sz;
            auto& v = right[rsz];
            auto itr = lower_bound(v.begin(), v.end(), b);
            if (itr != v.end()) res = min(res, abs(sum - 2 * (a + (*itr))));
            if (itr != v.begin()) {
                auto it = itr; --it;
                res = min(res, abs(sum - 2 * (a + (*it))));
            }
        }
    }

    return res;

    // Complexity analysis 
    // Time : O(n) + O(2^N * N) + O(N) + O(N * 2^N * log(2^N)) 
    // Space : O(2^n) 
}

void p1() {
    // Problem 1 : Leetcode 2035. Partition Array Into Two Arrays to Minimize Sum Difference - https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/ 

    vector<int> arr = { -533,-416,-546,9,203,-94,-92,-262,-750,2,-858576,-78,-64,241664,490952,-64,758,-189,2007420,-642,135110,9,4,518530,905,-30,-72,-16,4955,1 };
    int diff = minimumDifference(arr);
    cout << diff << endl;
}

int minDifference(vector<int>& arr) {
    // Your code goes here
    int N = arr.size();
    int tsum = accumulate(arr.begin(), arr.end(), 0);

    vector<vector<bool>> dp(N, vector<bool>(tsum + 1, 0));

    for (int i = 0; i < N; i++) {
        dp[i][0] = true;
    }
    if (arr[0] <= tsum) dp[0][arr[0]] = true;

    for (int i = 1; i < N; i++) {
        for (int t = 1; t <= tsum; t++) {
            bool not_pick = dp[i - 1][t];
            bool pick = false;
            if (arr[i] <= t) pick = dp[i - 1][t - arr[i]];

            dp[i][t] = not_pick | pick;
        }
    }

    int out = (int)(1e9);

    for (int t = 0; t <= tsum / 2; t++) {
        if (dp[N - 1][t]) {
            out = min(out, abs(tsum - (2 * t)));
        }
    }

    return out;

    // Complexity analysis 
    // Time : O(N) + O(N) + O(N * tsum) + O(tsum) 
    // Space : O(N * tsum) 
}

void p2() {
    // Problem 2 : Geeksforgeeks Minimum sum partition - https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1 

    vector<int> arr = { -533,-416,-546,9,203,-94,-92,-262,-750,2,-858576,-78,-64,241664,490952,-64,758,-189,2007420,-642,135110,9,4,518530,905,-30,-72,-16,4955,1 };
    int diff = minDifference(arr);
    cout << diff << endl;
}


int main() {
    // Day 13 of DP 

    p1();

    p2();


    return 0;
}