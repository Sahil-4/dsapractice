#include <iostream>
#include <vector>

using namespace std;

int mySqrt(int x) {
    int ans = 1;

    for (long long i = 0; i * i <= x; i++) {
        int prod = i * i;
        if (prod <= x) ans = i;
    }

    return ans;
}

void p1() {
    // P1 LC 69. Sqrt(x) - https://leetcode.com/problems/sqrtx/description/ 
    
    // int sq = mySqrt(5);
    // int sq = mySqrt(0);
    // int sq = mySqrt(1);
    int sq = mySqrt(2);

    cout << sq << endl;
}

int findPeakElement(vector<int>& nums) {
    if (nums.size() == 1) return 0;
    if (nums.size() == 2) return nums[0] > nums[1] ? 0 : 1;

    // peak element : nums[n], if nums[n-1] < nums[n] && nums[n] > nums[n+1] is true 
    // if n is 0 assume nums[n - 1] to be -INFINITY 
    // if n is last index assume nums[n + 1] to be -INFINITY 

    int n = nums.size() - 1;
    int l = 0, h = n;
    int m = l + (h - l) / 2;

    while (l <= h) {
        if ((m == 0 || nums[m] > nums[m - 1]) && (m == n || nums[m] > nums[m + 1])) return m;
        else if (m == 0 || nums[m] > nums[m - 1]) l = m + 1;
        else h = m - 1;

        m = l + (h - l) / 2;
    }

    return -1;
}

void p2() {
    // P2 LC 162. Find Peak Element - https://leetcode.com/problems/find-peak-element/ 

    // vector<int> nums = {1, 2, 4};
    vector<int> nums = {5, 3, 1};

    int peak = findPeakElement(nums);

    cout << peak << endl;
}

int main() {
    // Day 21 

    p1();

    p2();


    return 0;
}