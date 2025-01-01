#include <iostream>
#include <vector>
#include <map>

using namespace std;

int majorityElement(vector<int>& nums) {
    int major = 0, freq = 0;

    for (int i = 0; i < nums.size(); i++) {
        if (freq == 0) major = nums[i];

        if (nums[i] == major) freq++;
        else freq--;
    }

    // return major;

    // case : if it is not sure that there must be a majority element in the array 
    freq = 0;
    for (int i = 0; i < nums.size(); i++) if (nums[i] == major) freq++;

    if (freq > nums.size() / 2) return major;
    return -1;
}

void p1() {
    // Problem 1 : Leetcode 169. Majority Element - https://leetcode.com/problems/majority-element/description/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/majority-element-1587115620/1 

    vector<int> arr = {1,1,2,3,1,4,1};
    int m = majorityElement(arr);
}

int subarraySum(vector<int>& nums, int k) {
    int subArrCount = 0;

    int sum = 0;
    map<int, int> prefixSum; // sum, count 
    prefixSum.insert({0, 1});

    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];

        int need = sum - k;
        if (prefixSum.find(need) != prefixSum.end()) subArrCount += prefixSum[need];
        prefixSum[sum]++;
    }

    return subArrCount;
}

void p2() {
    // Problem 2 : Leetcode 560. Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/description/ 
    // GeeksForGeeks - https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1 

    vector<int> arr = {1, -1, 0};
    int k = 0;
    int subArrs = subarraySum(arr, k);
    cout << "subArrs :: " << subArrs << endl;
}

int main() {
    // Day 14 

    p1();

    p2();


    return 0;
}