#include <iostream>
#include <vector>

using namespace std;

vector<int> subarraySum(vector<int>arr, int n, long long s) {
    // Your code here 
    int windowStart = 0;
    int windowLast = 0;
    long long sum = arr[windowStart];

    if (sum == s) return {windowStart + 1, windowLast + 1};

    for (int i = 1; i < n; i++) {
        sum += arr[i];
        windowLast = i;

        while (sum > s && windowStart < windowLast) sum -= arr[windowStart++];
        if (sum == s) return {windowStart + 1, windowLast + 1};
    }

    return {-1 };
}

void p1() {
    // Problem 1 : Sub array with given sum - https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1 

    // vector<int> arr = {1, 2, 3, 4};
    // vector<int> arr = {135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134};
    vector<int> arr = {1, 2, 3, 4};
    long long sum = 0;

    vector<int> ans = subarraySum(arr, arr.size(), sum);
    cout << "start : " << ans[0] << " end : " << ans[1] << endl;
}

int main() {
    // Day 23 

    p1();


    return 0;
}