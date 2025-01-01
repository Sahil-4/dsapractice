#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int minSubArrayLen_Solution1(int target, vector<int>& nums) {
    int len = INT_MAX;
    int sum = 0;

    for (int l = 0, r = 0; r < nums.size(); r++) {
        sum += nums[r];

        while (sum >= target) {
            if (sum >= target && len > (r - l + 1)) len = r - l + 1;

            sum -= nums[l];
            l++;
        }
    }

    if (len == INT_MAX) return 0;
    return len;

    // Complexity analysis 
    // Time : O(n) 
    // Space : O(1) 
}

bool isSubArrExists(vector<int> &nums, int target, int windowLen) {
    int sum = 0;

    // init 
    for (int i = 0; i < windowLen; i++) sum += nums[i];
    if (sum >= target) return true;

    // window move 
    for (int l = 0, r = windowLen; r < nums.size(); l++, r++) {
        sum -= nums[l];
        sum += nums[r];
        if (sum >= target) return true;
    }

    return sum >= target;
}

int minSubArrayLen(int target, vector<int>& nums) {
    int len = INT_MAX;

    int low = 1, high = nums.size();

    while (low <= high) {
        int mid = low + (high - low) / 2;

        bool check = isSubArrExists(nums, target, mid);
        if (check) high = mid - 1, len = min(len, mid);
        else low = mid + 1;
    }

    return len == INT_MAX ? 0 : len;

    // Complexity analysis 
    // Time : O(n * log(n)) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 209. Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/ 
    // Geeksforgeeks - https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1 

    vector<int> nums = {2, 1, 3, 5, 1, 2, 3};
    int target = 5;

    int windowLen = minSubArrayLen(target, nums);
    cout << "windowLen :: " << windowLen << endl;
}

int main() {
    // Day 3 

    p1();


    return 0;
}