#include <bits/stdc++.h>

using namespace std;

class Problem1 {
    int solve1(vector<int>& arr) {
        int msum = arr[0], tsum = arr[0];

        for (int j = 1; j < arr.size(); j++) {
            tsum = max(tsum + arr[j], arr[j]);
            msum = max(msum, tsum);
        }

        return msum;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

    // this denotes different state of array (or part of array) (max sum on left, max sum on right, max subarray sum, whole array sum) 
    struct val {
        // left, sub, right, whole 
        int l, m, r, s;
        val(int l, int m, int r, int s) :l(l), m(m), r(r), s(s) {}
    };

    val solve2(vector<int>& arr, int i, int j) {
        if (i > j) { return val(0, 0, 0, 0); }
        if (i == j) { return val(arr[i], arr[i], arr[i], arr[i]); }

        int mid = i + (j - i) / 2;

        val lf = solve2(arr, i, mid);
        val rt = solve2(arr, mid + 1, j);

        int l, m, r, s;

        s = lf.s + rt.s;
        l = max(lf.l, lf.s + rt.l);
        r = max(rt.r, lf.r + rt.s);
        m = max(lf.r + rt.l, max(lf.m, rt.m));

        return val(l, m, r, s);

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(log(N)) stack 
    }

public:
    vector<int> findSubarray(vector<int>& arr) {
        // code here

        int n = arr.size();

        int msum = INT_MIN;
        int tsum = 0;

        int sindex = 0, eindex = 0;
        int tstartindex = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] < 0) {
                tsum = 0;
                continue;
            }

            if (tsum == 0) tstartindex = i;

            tsum += arr[i];

            if (msum < tsum || (msum == tsum && i - tstartindex > eindex - sindex)) {
                msum = tsum;
                sindex = tstartindex;
                eindex = i;
            }

            if (tsum < 0) {
                tsum = 0;
            }
        }

        vector<int> v = { arr.begin() + sindex, arr.begin() + eindex + 1 };

        if (v.size() == 1 && v[0] < 0) return { -1 };
        return v;

        // Complexity analysis 
        // Time : O(N) 
        // Space : O(1) 
    }

    int maxSubArray(vector<int>& arr) {
        // return solve1(arr);

        return solve2(arr, 0, arr.size() - 1).m;
    }
};

void p1() {
    // Problem 1 : Leetcode 53. Maximum Subarray - https://leetcode.com/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/maximum-sub-array5443/1 

    vector<int> arr = { -2,1,-3,4,1,-3,4,-1,1,-3,4,-1,2,1,-5,4,2,1,-5,4,-1,2,1,-5,4 };
    cout << Problem1().maxSubArray(arr);
}

class Problem2 {
    const int MAX_BOUND = 3 * 10000 + 1;
    const int MIN_BOUND = -3 * 10000 - 1;

    int solve1(vector<int>& nums) {
        int msum = INT_MIN;
        vector<int> msumarr;

        for (int start = 0, n = nums.size(); start < n; start++) {
            int tsum = 0;
            vector<int> tsumarr;

            for (int starti = 0; starti < n; starti++) {
                int index = (start + starti) % n;

                tsum += nums[index];
                tsumarr.push_back(nums[index]);
                if (msum < tsum) {
                    msum = tsum;
                    msumarr = tsumarr;
                }
            }
        }

        for (int e: msumarr) cout << e << " ";
        return msum;

        // Complexity analysis 
        // Time : O(N^2) 
        // Space : O(1) 
    }

    int kadanesMax(vector<int>& arr) {
        // max sum, temp max sum 
        int msum = MIN_BOUND, tsum = MIN_BOUND;

        for (int e: arr) {
            tsum = max(tsum+e, e);
            msum = max(msum, tsum);
        }

        return msum;
    }

    int kadanesMin(vector<int>& arr) {
        // min sum, temp min sum 
        int msum = MAX_BOUND, tsum = MAX_BOUND;

        for (int e: arr) {
            tsum = min(tsum+e, e);
            msum = min(msum, tsum);
        }

        return msum;
    }

    int solve2(vector<int>& arr) {
        // sum of entire array 
        int totalsum = accumulate(arr.begin(), arr.end(), 0);

        // max sum (straight sub array) 
        int maxsum = kadanesMax(arr);
        // min sum (straight sub array) 
        int minsum = kadanesMin(arr);

        // Maximum Sum Circular Subarray Sum 
        int mscssum = totalsum - minsum;

        // output 
        return maxsum < 0 ? maxsum : max(mscssum, maxsum);

        // Complexity analysis 
        // Time : O(3N) 
        // Space : O(1) 
    }

public:
    int maxSubarraySumCircular(vector<int>& nums) {
        // return solve1(nums);

        return solve2(nums);
    }
};

void p2() {
    // Problem 2 : Leetcode 918. Maximum Sum Circular Subarray - https://leetcode.com/problems/maximum-sum-circular-subarray/description/?envType=study-plan-v2&envId=top-interview-150 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1 

    vector<int> arr = { -1,-1,-1 };
    cout << Problem2().maxSubarraySumCircular(arr) << endl;
}


int main() {
    // Day 6 of February 

    p1();

    p2();


    return 0;
}