#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define mod 1000000007

// Solution 1 code 
int sumMaxMin(vector<int> myNumsArr) {
    int mini = myNumsArr[0];
    int maxi = myNumsArr[0];

    for (int i = 1; i < myNumsArr.size(); i++) {
        mini = min(mini, myNumsArr[i]);
        maxi = max(maxi, myNumsArr[i]);
    }

    return ((mini % mod) + (maxi % mod)) % mod;
}

int numSubseq(vector<int>& nums, int target, vector<int> myNumsArr, int index) {
    if (index == nums.size()) {
        if (myNumsArr.size() != 0 && sumMaxMin(myNumsArr) <= target) return 1;
        else return 0;
    }

    int a = numSubseq(nums, target, myNumsArr, index + 1);
    myNumsArr.push_back(nums[index]);
    int b = numSubseq(nums, target, myNumsArr, index + 1);

    return ((a % mod) + (b % mod)) % mod;
}

int numSubseq_solution1(vector<int>& nums, int target) {
    return numSubseq(nums, target, { }, 0);
    // TLE + MLE 
}


// Solution 2 code 

int myPow(int x, int n) {
    if (n == 0) return 1;
    if (n == 1) return x;

    long long ans = myPow(x, n/2);
    ans = ((ans % mod) * (ans % mod)) % mod;
    if (n & 1) ans = ((ans % mod) * (x % mod)) % mod;

    return ans % mod;
}

int sumMaxMin(int mini, int maxi) {
    return ((mini % mod) + (maxi % mod)) % mod;
}

int numSubseq(vector<int>& nums, int target, int low, int high) {
    if (high < low) return 0;
    int sum = sumMaxMin(nums[low], nums[high]);
    if (sum > target) return numSubseq(nums, target, low, high - 1);

    int a = myPow(2, high - low);
    int b = numSubseq(nums, target, low + 1, high);

    return ((a % mod) + (b % mod)) % mod;
}

int numSubseq(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    return numSubseq(nums, target, 0, nums.size() - 1);
}

void p1() {
    // Problem 1 : Leetcode 1498. Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/ 

    vector<int> nums = {};
    int target = 100;

    // int sseqs = numSubseq_solution1(nums, target);
    int sseqs = numSubseq(nums, target);
    cout << sseqs << endl;
}


int main() {
    // Day 21 

    p1();


    return 0;
}