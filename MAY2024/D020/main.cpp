#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <limits.h>

using namespace std;

vector<int> maxSlidingWindow_Solution1(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> ans;

    for (int it = 0; it <= n - k; it++) {
        int maxx = INT_MIN;
        int start = it, end = it + k;

        for (int it2 = start; it2 < end; it2++) {
            if (maxx < nums[it2]) maxx = nums[it2];
        }

        ans.push_back(maxx);
    }

    return ans;

    // !TLE 
}

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;
    vector<int> ans;

    for (int i = 0; i < nums.size(); i++) {
        while (!dq.empty() && dq.front() <= i - k) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] < nums[i]) dq.pop_back();

        dq.push_back(i);

        if (i >= k - 1) ans.push_back(nums[dq.front()]);
    }

    return ans;
}

void p1() {
    // Problem 1 : Leetcode 239. Sliding Window Maximum - https://leetcode.com/problems/sliding-window-maximum/ 

    vector<int> nums = {1, 10, -10, 5, 10, 12, 5, 13, 7, 2};
    int k = 5;

    vector<int> maxxs = maxSlidingWindow(nums, k);
    for (int i = 0; i < maxxs.size(); i++) cout << maxxs[i] << " ";
    cout << endl;
}

vector<long long> printFirstNegativeInteger_Solution1(long long int A[], long long int N, long long int K) {
    // Code here 
    vector<long long>ans;

    for (long long int i = 0; i <= N - K; i++) {
        int neg = 0;

        for (long long int j = i; j < i + K; j++) {
            if (A[j] < 0) {
                neg = A[j];
                break;
            }
        }

        ans.push_back(neg);
    }

    return ans;

    // !TLE 
}

vector<long long> printFirstNegativeInteger_Solution2(long long int A[], long long int N, long long int K) {
    // Code here 
    vector<long long> ans;
    vector<long long int> negs;

    for (long long int i = 0; i < N; i++) {
        if (A[i] < 0) negs.push_back(i);
    }
    reverse(negs.begin(), negs.end());

    for (long long int i = 0; i <= N - K; i++) {
        while (!negs.empty() && negs.back() < i) negs.pop_back();
        if (!negs.empty() && negs.back() < i + K) ans.push_back(A[negs.back()]);
        else ans.push_back(0);
    }

    return ans;

    // Space Comp : O(N) 
}

vector<long long> printFirstNegativeInteger(long long int A[], long long int N, long long int K) {
    // Code here 
    vector<long long> ans;
    deque<long long int> dq;
    long long int i = 0;

    // first 
    for (i = 0; i < K; i++) if (A[i] < 0) dq.push_back(i);

    // before last window 
    for (; i < N; i++) {
        if (!dq.empty()) ans.push_back(A[dq.front()]);
        else ans.push_back(0);

        // remove out of bounds 
        while (!dq.empty() && dq.front() < i - K + 1) dq.pop_front();
        
        // add curr index if element is negative 
        if (A[i] < 0) dq.push_back(i);
    }

    // last window 
    if (!dq.empty()) ans.push_back(A[dq.front()]);
    else ans.push_back(0);

    return ans;
}

void p2() {
    // Problem 2 : Geeksforgeeks First negative integer in every window of size k - https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1 

    long long int A[] = {-8, 2, 3, -6, 10};
    long long int N = 5;
    long long int K = 2;
    vector<long long> fn = printFirstNegativeInteger(A, N, K);
    for (int i = 0; i < fn.size(); i++) cout << fn[i] << " "; // -8 0 -6 -6
    cout << endl;
}

int main() {
    // Day 20 

    p1();

    p2();


    return 0;
}