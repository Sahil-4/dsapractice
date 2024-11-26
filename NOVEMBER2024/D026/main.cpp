#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> tabulation(vector<int>& arr, int N) {
    sort(arr.begin(), arr.end());

    vector<int> dp(N, 1);
    vector<int> path(N);

    for (int index = 0; index < N; index++) {
        path[index] = index;

        for (int prev = 0; prev < index; prev++) {
            if ((arr[index] % arr[prev] == 0) && (dp[index] < 1 + dp[prev])) {
                dp[index] = 1 + dp[prev];
                path[index] = prev;
            }
        }
    }

    int idx = 0;
    for (int i = 0; i < N; i++) {
        if (dp[i] > dp[idx]) idx = i;
    }

    vector<int> LIS;
    LIS.push_back(arr[idx]);
    while (path[idx] != idx) {
        idx = path[idx];
        LIS.push_back(arr[idx]);
    }

    return LIS;

    // Complexity analysis 
    // Time : O(N*LOG(N)) + O(N*N) + O(N) + O(N) 
    // Space : O(2N) for memory 
}

void p1() {
    // Problem 1 : Leetcode 368. Largest Divisible Subset - https://leetcode.com/problems/largest-divisible-subset/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/largest-divisible-subset--170643/1 

    vector<int> nums = { 1,2,4,8 };

    vector<int> LDS = tabulation(nums, nums.size());
    for (int i = 0; i < LDS.size(); i++) {
        cout << LDS[i] << " ";
    } cout << endl;
}


int main() {
    // Day 26 of DP 

    p1();


    return 0;
}