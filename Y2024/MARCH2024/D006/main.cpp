#include <iostream>
#include <vector>

using namespace std;

int maxSubArray(vector<int>& nums) {
    // edge - if array has only one element 
    if (nums.size() == 1) return nums[0];

    // kadane
    int sum = 0;
    int temp_sum = 0;

    for (int i = 0; i < nums.size(); i++) {
        temp_sum += nums[i];

        if (temp_sum < 0) temp_sum = 0;
        if (sum < temp_sum) sum = temp_sum;
    }

    // if everything goes well - kadange is able to find answer 
    if (sum != 0)  return sum;

    // possible that there are only negatives 
    // for this we will have to consider smallest negative (subarray of size 1)
    sum = nums[0];
    for (int i = 0; i < nums.size(); i++) {
        if (sum < nums[i]) sum = nums[i];
    }

    // minimum negative number 
    return sum;

    // should be solved using DP 
    // here is solved using kadane and a loop 
}

void p1() {
    // Problem 1 : Maximum Subarray - https://leetcode.com/problems/maximum-subarray/description/ 

    // vector<int> arr = {-2,1,-3,4,-1,2,1,-5,4};
    vector<int> arr = {-2,1};

    int size = maxSubArray(arr);
    cout << size << endl;
}

int main() {
    // Day 6 

    p1();


    return 0;
}