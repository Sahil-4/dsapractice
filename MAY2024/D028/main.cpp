#include <iostream>
#include <vector>
#include <map>

using namespace std;

int numSubarraysWithSum_Solution1(vector<int>& nums, int goal) {
    int count = 0;

    for (int it = 0; it < nums.size(); it++) {
        int sum = 0;

        for (int it2 = it; it2 < nums.size(); it2++) {
            sum += nums[it2];

            if (sum == goal) count++;
            if (sum > goal) break;
        }
    }

    return count;

    // Complexity 
    // Time : O(n ^ 2) 
    // Space : O(1) 
}

int numSubarraysWithSum_Solution2(vector<int>& nums, int goal) {
    int n = nums.size();
    int subarraysCount = 0;

    map<int, int> prefixSumFreqTable;
    int sum = 0;

    prefixSumFreqTable.insert({sum, 1});

    for (int it = 0; it < n; it++) {
        sum += nums[it];

        int need = sum - goal;
        if (prefixSumFreqTable.find(need) != prefixSumFreqTable.end()) subarraysCount += prefixSumFreqTable[need];

        if (prefixSumFreqTable.find(sum) != prefixSumFreqTable.end()) prefixSumFreqTable[sum]++;
        else prefixSumFreqTable.insert({sum, 1});
    }

    return subarraysCount;

    // ! USING PREFIX SUM 
    // Complexity 
    // Time : O(n) 
    // Space : O(n) 
}

int numSubarraysWithSum(vector<int>& nums, int goal) {
    int n = nums.size();
    int subarraysCount = 0;

    int l = 0, r = 0;
    int sum = 0;
    int zeroes = 0;

    while (r < n) {
        sum += nums[r];

        // sum exceeds the goal 
        while (l < r && (nums[l] == 0 || sum > goal)) {
            if (nums[l] == 0) zeroes++;
            else zeroes = 0;

            sum -= nums[l];
            l++;
        }

        // sum is equal to goal 
        if (sum == goal) subarraysCount += 1 + zeroes;

        r++;
    }

    return subarraysCount;
    // ! TWO POINTER APPROACH 
    // Complexity 
    // Time : O(2 * n) 
    // Space : O(1) 
}

void p1() {
    // Problem 1 : Leetcode 930. Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/ 

    vector<int> nums = {1, 0, 1, 1, 0, 0, 1};
    int goal = 2;

    int subArrCount = numSubarraysWithSum(nums, goal);
    cout << "subArrCount :: " << subArrCount << endl;
}

int main() {
    // Day 28 

    p1();


    return 0;
}