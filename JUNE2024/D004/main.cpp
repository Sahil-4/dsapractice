#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int findKthLargest_Solution1(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    return nums[nums.size() - k];

    // Complexity analysis - using sorting 
    // Time : O(n * log(n)) + O(1) 
    // Space : O(1) 
}

int findKthLargest_Solution2(vector<int>& nums, int k) {
    // run a loop k times 
    for (k; k > 0; k--) {
        // find the biggest element index in nums array 
        int biggest_index = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[biggest_index] < nums[i]) biggest_index = i;
        }

        // return biggest element if k is 1 
        if (k == 1) return nums[biggest_index];

        // remove the biggest element from nums array 
        nums.erase(nums.begin() + biggest_index);
    }

    return -1;

    // Complexity analysis - brute force 
    // Time : O(k) * O(n) 
    // Space : O(1) 
}

int findKthLargest(vector<int>& nums, int k) {
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < nums.size(); i++) {
        pq.push(nums[i]);

        if (pq.size() > k) pq.pop(); // log(k) 
    }

    return pq.top();

    // Complexity analysis - using heap 
    // Time : O(n * log(n)) 
    // Space : O(k) 
}

void p1() {
    // Problem 1 : Leetcode 215. Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/ 

    vector<int> nums = {2, 6, 7, 2, 5, 4, 2, 54};
    int k = 5;

    int gt = findKthLargest(nums, k);
    cout << "gt :: " << gt << endl;
}

int main() {
    // Day 4 

    p1();


    return 0;
}