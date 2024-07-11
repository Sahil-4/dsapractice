#include <iostream>
#include <vector>
#include <stack>

using namespace std;

long long subArrayRanges_Solution1(vector<int>& nums) {
    int n = nums.size();
    long long sum = 0;

    for (int i = 0; i < n; i++) {
        int mini = nums[i];
        int maxi = nums[i];

        for (int j = i; j < n; j++) {
            mini = min(mini, nums[j]);
            maxi = max(maxi, nums[j]);

            int diff = maxi - mini;
            sum += diff;
        }
    }

    return sum;

    // complexity analysis 
    // Time : O(n ^ 2) 
    // Space : O(1) 
}

vector<int> nextSmallLeft(vector<int>& arr, int n) {
    vector<int> out(n, -1);
    stack<int> stk;

    for (int i = 0; i < n; i++) {
        while (!stk.empty() && arr[stk.top()] >= arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top();
        stk.push(i);
    }

    return out;
}

vector<int> nextSmallRight(vector<int>& arr, int n) {
    vector<int> out(n, n);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] > arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top();
        stk.push(i);
    }

    return out;
}

long long subArrayMinimumSum(vector<int>& arr, int n) {
    long long sum = 0;
    vector<int> nsl = nextSmallLeft(arr, n);
    vector<int> nsr = nextSmallRight(arr, n);

    for (int i = 0; i < n; i++) {
        long long el = arr[i], l = nsl[i], r = nsr[i];

        long long subarrs = (i - l) * (r - i);
        long long prod = subarrs * el;

        sum += prod;
    }

    return sum;
}

vector<int> nextGreaterLeft(vector<int>& arr, int n) {
    vector<int> out(n, -1);
    stack<int> stk;

    for (int i = 0; i < n; i++) {
        while (!stk.empty() && arr[stk.top()] <= arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top();
        stk.push(i);
    }

    return out;
}

vector<int> nextGreaterRight(vector<int>& arr, int n) {
    vector<int> out(n, n);
    stack<int> stk;

    for (int i = n - 1; i >= 0; i--) {
        while (!stk.empty() && arr[stk.top()] < arr[i]) stk.pop();

        if (!stk.empty()) out[i] = stk.top();
        stk.push(i);
    }

    return out;
}

long long subArrayMaximumSum(vector<int>& arr, int n) {
    long long sum = 0;
    vector<int> ngl = nextGreaterLeft(arr, n);
    vector<int> ngr = nextGreaterRight(arr, n);

    for (int i = 0; i < n; i++) {
        long long el = arr[i], l = ngl[i], r = ngr[i];

        long long subarrs = (i - l) * (r - i);
        long long prod = el * subarrs;

        sum += prod;
    }

    return sum;
}

long long subArrayRanges(vector<int>& nums) {
    int n = nums.size();
    return subArrayMaximumSum(nums, n) - subArrayMinimumSum(nums, n);

    // complexity analysis 
    // Time : O(n), overall 
    // Space : O(n), overall 
}

void p1() {
    // Problem 1 : Leetcode 2104. Sum of Subarray Ranges - https://leetcode.com/problems/sum-of-subarray-ranges/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/sum-of-subarray-ranges/1 

    vector<int> arr = {1, 2, 5, 1};
    int sum = subArrayRanges(arr);
    cout << "sum ::" << sum << endl;
}


int main() {
    // Day 11 

    p1();


    return 0;
}