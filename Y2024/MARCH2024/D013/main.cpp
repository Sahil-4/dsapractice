#include <iostream>
#include <vector>
#include <map>

using namespace std;

int subarraySum_bruteForce(vector<int>& nums, int k) {
    int count = 0;

    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums[j];
            if (sum == k) count++;
        }
    }

    return count;

    // T = O(n * n) 
    // S = O(1) 
}

int subarraySum(vector<int>& nums, int k) {
    // using prefix sum 

    int count = 0;
    int prefixSum = 0;

    // hashmap to store prefix sums s - k 
    map<int, int> ps;
    ps[0] = 1;

    for (int i = 0; i < nums.size(); i++) {
        prefixSum += nums[i];

        int need = prefixSum - k;
        count += ps[need];
        ps[prefixSum] += 1;
    }

    return count;

    // T = O(n) 
    // S = O(n) 
}

void p1() {
    // Problem 1 : Subarray with sum K - https://leetcode.com/problems/subarray-sum-equals-k/description/  

    vector<int> nums = {1, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 40, 0, 5, 7, -5, -200, -12, 13, 8, 54, 50, 1, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 40, 0, 5, 7, -5, -200, -12, 13, 8, 54, 50, 1, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 40, 0, 5, 7, -5, -200, -12, 13, 8, 54, 50, 1, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 5, 13, 7, -1, 2, 5, -7, 18, 13, 15, 2, -2, 0, 5, -13, 15, 18, 21, 20, 40, 0, 5, 7, -5, -200, -12, 13, 8, 54, 50};

    int sum = 15;
    int c = subarraySum(nums, sum);

    cout << c << endl;
}

int main() {
    // Day 13 

    p1();


    return 0;
}