#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int findMin(vector<int>& nums) {
    if (nums.size() == 1) return nums[0];
    if (nums[0] < nums[nums.size() - 1]) return nums[0];
    if (nums[0] > nums[nums.size() - 1] && nums[nums.size() - 1] < nums[nums.size() - 2]) return nums[nums.size() - 1];

    int l = 0, h = nums.size() - 1;
    int m = l + (h - l) / 2;

    while (l < h) {
        if (nums[m] < nums[m - 1] && nums[m] < nums[m + 1]) return nums[m];
        else {
            if (nums[m] > nums[l]) l = m;
            else h = m;
        }

        m = l + (h - l) / 2;
    }

    return -1;
}

void p1() {
    // Probelm 1 : 153. Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description 

    // vector<int> arr = {1, 2, 3, 4, 5};
    // vector<int> arr = { 2, 3, 4, 5, 1};
    // vector<int> arr = {4, 5, 1, 2, 3};
    // vector<int> arr = {1};
    // vector<int> arr = {5, 1, 2, 3, 4};
    vector<int> arr = {3, 4, 5, 1, 2};

    int m = findMin(arr);
    cout << m << endl;
}

int maxProfit(vector<int>& prices) {
    // DP 
    int profit = 0;
    int minPrice = INT_MAX;

    for (int i = 0; i < prices.size(); i++) {
        if (prices[i] < minPrice) minPrice = prices[i];
        profit = max(profit, prices[i] - minPrice);
    }

    return profit;
}

void p2() {
    // Problem 2 : Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/ 

    vector<int> prices = {7,1,5,3,6,4};
    int p = maxProfit(prices);
    cout << p << endl;
}

int main() {
    // Day 7 

    p1();

    p2();


    return 0;
}