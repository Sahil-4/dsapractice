#include <iostream>
#include <vector>

using namespace std;

void rotate(vector<int>& nums, int k) {
    // [1,2,3,4,5,6,7], k = 3
    // [5,6,7,1,2,3,4] 
    // last k elements will come in start 
    // [1,2,3,4,5,6,7] 
    // [1,2,3,4],[5,6,7]
    // [5,6,7],[1,2,3,4]
    // [5,6,7,1,2,3,4]

    // [1,2,3,4,5,6,7], k = 3
    // take last k elements 
    // [5,6,7]
    // reverse them 
    // [7,6,5]
    // take other elements and reverse them as well 
    // [1,2,3,4] -> [4,3,2,1]
    // combine both these arrays 
    // [7,6,5,4,3,2,1]

    k = k % nums.size();

    if (k == 0) return;

    int i = 0;
    int j = nums.size() - 1 - k;
    while (i < j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;

        i++;
        j--;
    }

    i = nums.size() - k;
    j = nums.size() - 1;

    while (i < j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;

        i++;
        j--;
    }

    i = 0;
    j = nums.size() - 1;
    while (i < j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;

        i++;
        j--;
    }
}

void p1() {
    // Problem 1 : 189. Rotate Array - https://leetcode.com/problems/rotate-array/description/ 

    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int k = 5;

    rotate(nums, k);

    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
}


int main() {
    // Day 1 of March overall 61st day 
    p1();


    return 0;
}